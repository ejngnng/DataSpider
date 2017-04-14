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
import re

def getTargetUrl():
    start_urls = []
    for i in range(1, 2042):
        start_urls.append('http://wuliu.6-china.com/freight/carlist/p' + str(i) + '.html')
    return start_urls


def buildUrl(aTag):
    domain = 'http://wuliu.6-china.com'
    url = domain + aTag
    print('targetUrl: ' + url)
    return url

def getAtag(response):
    page = BeautifulSoup(response.data, 'lxml')
    targetLink = page.find_all('a', href=re.compile('/freight/cardetail-'))
    return targetLink
    # for link in targetLink:
    #     dataLink.append(buildUrl(link))

def parseData(response):
    data = []
    page = BeautifulSoup(response.data, 'lxml')
    dataClass = page.find_all(class_='photo')
    for item in dataClass:
        targetItem = item.find_all('li')
        for txt in targetItem:
            data.append(txt.get_text())
