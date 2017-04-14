#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
#
# Description: common file for global var and user-agent
#
# Author:      ninja
#
# Date:        created by 2017-04-10
#
###################################################

import threading
import queue
import time
from Spider import China6
from common import download
from bs4 import BeautifulSoup
from Dao import MysqlPipeline
import random

class ProducerUrl(threading.Thread):
    def __init__(self, threadName, dataQue):
        threading.Thread.__init__(self, name=threadName)
        self.dataQ = dataQue

    def run(self):
        print("start get target link")
        startUrls = China6.getTargetUrl()
        for urls in startUrls:
            print('ProducerUrls')
            print('urls: ' + urls)
            response = download.downloader(url=urls)
            targetLink = China6.getAtag(response)
            for link in targetLink:
                self.dataQ.put(China6.buildUrl(link.get('href')))
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
            page = BeautifulSoup(response.data, 'lxml')
            dataClass = page.find_all(class_='photo')
            data = []
            for item in dataClass:
                targetItem = item.find_all('li')
                for txt in targetItem:
                    targetData = txt.get_text()
                    print('targetData: ' + targetData)
                    data.append(targetData)
                self.dataQ.put(data)
            time.sleep(random.randint(1, 5))

class InsertDB(threading.Thread):
    def __init__(self, threadName, dataQue):
        threading.Thread.__init__(self, name=threadName)
        self.dataQ = dataQue

    def run(self):

        while True:
            print('insert data')
            item = self.dataQ.get()
            conn = MysqlPipeline.connectDB()
            MysqlPipeline.insert_data(conn, item)

def main():
    urlQueue = queue.Queue()
    itemQueue = queue.Queue()
    Producer = ProducerUrl('Pro', dataQue=urlQueue)
    Parser = ParserResponse('Par', urlQue=urlQueue, dataQue=itemQueue)
    Pipline = InsertDB('Insert', dataQue=itemQueue)
    Producer.start()
    Parser.start()
    Pipline.start()

    # Producer.join()
    # Parser.join()
    # Pipline.join()


if __name__ == '__main__':
    main()
