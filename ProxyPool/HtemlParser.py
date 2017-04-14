#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
#
# Description: get proxy resource
#
# Author:      ninja
#
# Date:        created by 2017-04-10
#
###################################################

from common.download import downloader
from bs4 import BeautifulSoup
import telnetlib
import Dao

class HtmlParse:
    def __init__(self):
        self.__proxyList = []
        self.__valiedProxy = []
        self.__targetUrl = "http://www.xicidaili.com/nn"

    def getProxyList(self):
        return self.__proxyList

    def setProxyList(self, value):
        self.__proxyList = value

    def getValiedProxy(self):
        return self.__valiedProxy

    def findBs4(self, response):
        page = BeautifulSoup(response.data, 'lxml')
        trs = page.find('table', {"id": "ip_list"}).findAll('tr')
        count = 0
        for tr in trs[1:]:
            tds = tr.findAll('td')
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            location = tds[3].text.strip()
            protocol = tds[5].text.strip()
            count += 1
            #print("%d, ip: %s, port: %s, location: %s, protocol: %s" % (count, ip, port, location, protocol))
            item = [ip, port, location, protocol]
            self.getProxyList().append(item)

    def __constructProxy(self,item = []):
        proxy_url = item[3].lower() + '://' + item[0] + ':' + item[1]
        return proxy_url


    def check(self, response):
        #print('targetUrl : ' + self.__targetUrl)
        #response = downloader(url=self.__targetUrl)

        self.findBs4(response)

        proxyList = self.getProxyList()
        for proxy in proxyList:
            ip = proxy[0]
            port = proxy[1]
            try:
                telnetlib.Telnet(ip, port, timeout=10)
            except:
                print('connect failed: ' + self.__constructProxy(proxy))
            else:
                print('success: ' +  self.__constructProxy(proxy))
                self.__valiedProxy.append(proxy)
                Dao.insert_proxy_url(self.__constructProxy(proxy))

    def getProxy(self):
        print('targetUrl : ' + self.__targetUrl)
        response = downloader(url = self.__targetUrl)

        self.findBs4(response)
        proxyList = self.getProxyList()
        for proxy in proxyList:
            url = self.__constructProxy(proxy)
            isAlive = self.checkProxy(url)
            print(isAlive)
            if isAlive:
                print('varlied proxy: %s' % url)
                return url
            else:
                continue


def main():
    for pageNum in range(1, 1600):
        print(pageNum)
        proxy_url = "http://www.xicidaili.com/nn/" + str(pageNum)
        print('target URL:')
        print(proxy_url)
        response = downloader(url = proxy_url)
        paser = HtmlParse()
        paser.check(response)

