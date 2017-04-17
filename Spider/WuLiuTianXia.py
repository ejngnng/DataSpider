#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
#
# Description: website http://www.56885.net/
#
# Author:      ninja
#
# Date:        created by 2017-04-10
#
###################################################

from bs4 import BeautifulSoup
import re
from common import download
from Dao import MysqlPipeline
import threading
import queue
import time
import random

def getTargetUrl():
    start_urls = []
    for i in range(1466, 7137):
        start_urls.append('http://www.56885.net/cheyuan/?0_0_0_0_0_0_0_0_0_0_'+ str(i) + '.html')
    return start_urls

def getAtag(response):
    page = BeautifulSoup(response.data, 'lxml')
    targetLink = page.find_all('a', href=re.compile('../cheyuan/'))
    dataLink = []
    for index, link in enumerate(targetLink):
        if(index == 0):
            continue
        strLink = link.get('href')
        print('deal: ' + strLink.strip('..'))
        dataLink.append(buildUrl(strLink.strip('..')))

    return dataLink

def buildUrl(aTag):
    domain = 'http://www.56885.net'
    url = domain + aTag
    return url

def ParseData(response):
    data = []
    page = BeautifulSoup(response.data, 'lxml')
    dataClass = page.find_all('ul', class_='zxlists')
    for item in dataClass:
        targetItem = item.find_all('li')
        for txt in targetItem:
            data.append(txt.get_text())
    return data

def getItem(data):
    print("data len: " + str(len(data)))
    print("data:")
    for i, d in enumerate(data):
        print(str(i) + ':' + d)
    item = []
    dataLen = len(data)
    # location = ParseLocation(data[1])
    if(dataLen == 11):
        s1 = data[1].split('：')
        s2 = s1[1].split()
        print(s2)
        item.append('')         #carNum
        item.append(data[2])    #carType
        item.append(s2[0])      #startLocation
        item.append(s2[2])      #endLocation
        item.append(data[2])    #price
        item.append(data[4])    #carLen
        item.append(data[3])    #carLoad
        item.append(data[9])    #carAddr
        item.append(data[7])    #carContants
        item.append(data[8])    #phoneNum
        item.append(data[6])    #company
    if(dataLen == 12):
        s1 = data[2].split('：')
        s2 = s1[1].split()
        print(s2)
        item.append(data[0])    #carNum
        item.append(data[3])    #carType
        item.append(s2[0])      #startLocation
        item.append(s2[2])      #endLocation
        item.append(data[6])    #price
        item.append(data[5])    #carLen
        item.append(data[4])    #carLoad
        item.append(data[10])   #carAddr
        item.append(data[8])    #carContants
        item.append(data[9])    #phoneNum
        item.append(data[7])    #company
    return item

def ParseLocation(dataStr):
    #data = '车源线路：山东-淄博-市辖区(淄博市高青县) 到 四川-四川-市辖区'
    s1 = dataStr.split('：')
    s2 = s1[1].split()
    print(s2)
    return s2


class ProducerUrl(threading.Thread):
    def __init__(self, threadName, dataQue):
        threading.Thread.__init__(self, name=threadName)
        self.dataQ = dataQue

    def run(self):
        print("start get target link")
        startUrls = getTargetUrl()
        for urls in startUrls:
            print('ProducerUrls')
            print('urls: ' + urls)
            response = download.downloader(url=urls)
            targetLink = getAtag(response)
            for link in targetLink:
                self.dataQ.put(link)
            time.sleep(random.randint(3, 10))

class ParserResponse(threading.Thread):
    def __init__(self, threadName, urlQue):
        threading.Thread.__init__(self, name=threadName)
        self.urlQ = urlQue
    def run(self):
        conn = MysqlPipeline.connectDB()
        while True:
            print("parse response")
            urls = self.urlQ.get()
            print('ParserResponse urls')
            print('urls: ' + urls)
            response = download.downloader(url=urls)
            try:
                data = ParseData(response)
                MysqlPipeline.insert_dataWLTX(conn, getItem(data))
            except:
                pass
            time.sleep(random.randint(1, 5))
        MysqlPipeline.disconnectDB(conn)


def main():
    start_urls = getTargetUrl()
    for ul in start_urls:
        page = download.downloader(url=ul)
        targetLink = getAtag(page)
        conn = MysqlPipeline.connectDB()
        for link in targetLink:
            targetItem = download.downloader(url=link)
            data = ParseData(targetItem)
            item = getItem(data)
            MysqlPipeline.insert_dataWLTX(conn, item)
            time.sleep(random.randint(1, 5))
        MysqlPipeline.disconnectDB(conn)

if __name__ == '__main__':
    # start_url = getTargetUrl()
    # page = download.downloader(url=start_url)
    # dataLink = getAtag(page)
    # response = download.downloader(url=dataLink[0])
    # data = ParseData(response)
    # item = getItem(data)
    # conn = MysqlPipeline.connectDB()
    # MysqlPipeline.insert_dataWLTX(conn, item)
    # MysqlPipeline.disconnectDB(conn)
    main()
