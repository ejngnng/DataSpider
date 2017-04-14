#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
#
# Description: get China6 resource
#
# Author:      ninja
#
# Date:        created by 2017-04-10
#
###################################################

from bs4 import BeautifulSoup

class China6:

    start_urls = []
    domain = []
    dataLink = []
    item = []

    def __init__(self):
        for i in range(1, 2042):
            self.start_urls.append('http://wuliu.6-china.com/freight/carlist/' + str(i) + '.html')
        self.domain = 'http://wuliu.6-china.com'

    def getStartUrls(self):
        return self.start_urls

    def getDataLinks(self):
        return self.dataLink

    def buildUrl(self, aTag):
        url = self.domain + aTag
        return url

    def getAtag(self, response):
        page = BeautifulSoup(response.data, 'lxml')
        targetLink = page.find_all('a', href=re.compile('/freight/cardetail-'))

        for link in targetLink:
            self.__dataLink.append(self.buildUrl(link))

    def parseData(self, targetResponse):
        page = BeautifulSoup(response.data, 'lxml')
        dataClass = page.find_all(class_='photo')
        for item in dataClass:
            print(item)
            targetItem = item.find_all('li')
            for txt in targetItem:
                print(txt.get_text())
                self.item.append(txt.get_text())
