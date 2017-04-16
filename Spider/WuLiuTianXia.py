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
    for i in range(1, 7137):
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
    # location = ParseLocation(data[1])
    try:
        s1 = data[1].split('：')
        s2 = s1[1].split()
        print(s2)
        item.append(data[2])
        item.append(s2[0])
        item.append(s2[2])
        item.append(data[2])
        item.append(data[4])
        item.append(data[3])
        item.append(data[9])
        item.append(data[7])
        item.append(data[8])
        item.append(data[6])
    except:
        print('data error')
        pass
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
    def __init__(self, threadName, urlQue, dataQue):
        threading.Thread.__init__(self, name=threadName)
        self.dataQ = dataQue
        self.urlQ = urlQue
    def run(self):
        while True:
            print("parse response")
            urls = self.urlQ.get()
            print('ParserResponse urls')
            print('urls: ' + urls)
            response = download.downloader(url=urls)
            data = ParseData(response)
            self.dataQ.put(getItem(data))
            time.sleep(random.randint(1, 5))

class InsertDB(threading.Thread):
    def __init__(self, threadName, dataQue):
        threading.Thread.__init__(self, name=threadName)
        self.dataQ = dataQue

    def run(self):
        conn = MysqlPipeline.connectDB()
        while True:
            print('insert data')
            item = self.dataQ.get()
            MysqlPipeline.insert_dataWLTX(conn, item)
        MysqlPipeline.disconnectDB(conn)


def main():
    urlQueue = queue.Queue()
    itemQueue = queue.Queue()
    Producer = ProducerUrl('Pro', dataQue=urlQueue)
    Parser = ParserResponse('Par', urlQue=urlQueue, dataQue=itemQueue)
    Pipline = InsertDB('Insert', dataQue=itemQueue)
    Producer.start()
    Parser.start()
    Pipline.start()

    Producer.join()
    Parser.join()
    Pipline.join()

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
