#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
#
# Description: url request
#
# Author:      ninja
#
# Date:        created by 2017-04-05
#
###################################################

import urllib3
import json
import common


def download(proxy_url, url):
    http = urllib3.ProxyManager(proxy_url)
    r = http.request(
        'GET',
        url,
        headers=common.HEADER
    )
    data = json.loads(r.data.decode('utf-8'))
    print(data)
    return data

def getPage(url):
    http = urllib3.PoolManager()
    r = http.request(
        'GET',
        url,
        headers = common.HEADER
    )
    if(r.status != 200 ):
        print('not avaliable')
        return
    return r

def getPageByProxy(url, proxy):
    http = urllib3.ProxyManager(proxy)
    r = http.request(
        'GET',
        url,
        headers=common.HEADER
    )
    if(r.status != 200):
        print('not avaliable')
        return
    return r


def downloader(**kwargs):

    if kwargs.__len__() == 1:
        if 'url' in kwargs.keys():
            url = kwargs.__getitem__('url')
            print(url)
            data = getPage(url)
         #   print(json.loads(data.decode('utf-8')))
            return data
        else:
            print('need to set url')
            return
    elif kwargs.__len__() == 2:
        if 'url' and 'proxy' in kwargs.keys():
            url = kwargs.__getitem__('url')
            proxy = kwargs.__getitem__('proxy')
            print('url: %s' % url)
            print('proxy: %s' % proxy)
            data = getPageByProxy(url, proxy)
            return data
        else:
            print('need to set url and proxy')
    else:
        print('wrong parameters')


if __name__ == '__main__':
    #download('http://192.168.3.73/index.php/app/app/test?key=category')
    #download('http://static.meizi.app.m.letv.com/android/mod/mob/ctl/listalbum/act/index/src/1/cg/1/ph/420003,420004/pn/1/ps/5/pcode/010110263/version/5.6.2.mindex.html')
    downloader(url = 'http://192.168.3.73/index.php/app/app/test?key=category')