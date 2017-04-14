#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###################################################
#
# Description: common file for global var and user-agent
#
# Author:      ninja
#
# Date:        created by 2017-04-05
#
###################################################

import random

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

HEADER = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

ProxyURL = [
    "http://60.17.161.234:808",
    "http://175.23.38.125:28703",
    "http://183.27.124.4:49150",
    "http://27.159.124.186:8118",
    "http://221.216.94.77:808",
    "http://42.81.58.198:80",
    "http://61.191.173.31:808",
    "http://175.155.25.20:808",
    "http://27.199.91.227:47349",
    "http://221.10.159.234:1337",
    "http://171.39.93.13:8123",
    "http://114.216.227.25:808",
    "http://27.159.126.143:8118",
    "http://112.234.79.130:59533",
    "http://218.86.128.36:8118",
    "http://113.231.91.74:47489",
    "http://113.243.193.137:50099",
    "http://101.86.157.236:38904",
    "http://42.85.175.160:29417",
    "http://27.216.86.82:26835",
    "http://27.216.86.82:26835",
    "http://119.182.3.195:49110",
    "http://171.13.36.86:808",
    "http://110.73.7.133:8123",
    "http://14.110.243.234:44388",
    "http://59.57.223.211:28139",
    "http://119.109.152.233:42605",
    "http://171.38.128.48:8123",
    "http://110.73.11.244:8123",
    "http://119.5.0.19:808",
    "http://183.157.182.90:80",
    "http://122.228.179.178:80",
    "http://121.23.87.60:37474",
    "http://171.112.220.98:25463",
    "http://114.83.100.20:23452",
    "http://124.42.7.103:80",
    "http://59.62.211.222:33667",
    "http://111.122.155.121:51206",
    "http://120.90.6.92:8080",
    "http://175.150.100.32:10854",
    "http://124.88.67.14:80",
    "http://182.90.68.249:8123",
    "http://182.90.68.249:8123",
    "http://175.155.24.51:808",
    "http://183.60.111.229:808",
    "http://110.72.35.249:8123",
    "http://58.33.37.205:8118",
    "http://121.201.24.248:8088",
    "http://60.12.11.42:808",
    "http://119.5.0.80:808",
    "http://60.12.11.42:808",
    "http://119.163.121.122:8080",
    "http://60.12.11.42:808",
    "http://119.163.121.122:8080",
    "http://124.88.67.10:80",
    "http://175.155.25.55:808",
    "http://60.12.11.42:808",
    "http://119.163.121.122:8080",
    "http://110.73.3.216:8123",
    "http://171.13.37.48:808",
    "http://110.73.9.243:8123",
    "http://110.73.3.216:8123",
    "http://110.73.9.243:8123",
    "http://175.155.24.43:808",
    "http://182.88.204.133:8123",
    "http://119.254.84.90:80",
    "http://182.88.204.133:8123",
    "http://183.93.159.29:808",
    "http://114.239.146.73:808",
    "http://60.21.132.218:63000",
    "http://114.239.146.73:808",
    "http://119.5.1.53:808",
    "http://124.88.67.19:80",
    "http://119.5.0.55:808",
    "http://101.53.101.172:9999",
    "http://110.52.235.70:808",
    "http://110.52.235.70:808",
    "http://124.88.67.24:80",
    "http://124.88.67.17:82",
    "http://125.89.121.104:808",
    "http://182.38.110.31:808",
    "http://218.64.92.198:808",
    "http://121.226.162.2:808",
    "http://222.85.50.147:808",
    "http://125.89.121.104:808",
    "http://125.89.121.104:808",
    "http://180.166.27.171:8080",
    "http://117.43.1.115:808",
    "http://183.78.183.156:82",
    "http://115.213.241.102:808",
    "http://115.220.3.137:808",
    "http://36.249.29.166:808",
    "http://61.160.247.79:1080",
    "http://125.89.122.153:808",
    "http://121.40.40.182:80",
    "http://180.167.34.187:80",
    "http://183.63.223.2:63000",
    "http://222.94.150.46:808",
    "http://222.94.148.48:808",
    "http://123.169.88.237:808",
    "http://115.213.204.156:808",
    "http://203.93.0.115:80",
    "http://123.169.88.237:808",
    "http://218.4.101.130:83",
    "http://58.59.46.114:8080",
    "http://117.43.1.12:808",
    "http://58.59.46.114:8080",
    "http://124.88.67.23:80",
    "http://218.64.93.201:808",
    "http://111.155.124.67:8123",
    "http://124.88.67.13:80",
    "http://60.214.118.170:63000",
    "http://124.88.67.13:80",
    "http://222.85.39.121:808",
    "http://42.81.58.199:80",
    "http://124.88.67.13:80",
    "http://222.169.193.162:8099",
    "http://49.65.230.179:808",
    "http://49.65.230.179:808",
    "http://222.92.141.250:80",
    "http://222.169.193.162:8099",
    "http://222.169.193.162:8099",
    "http://14.152.39.185:8888",
    "http://110.73.0.239:8123",
    "http://171.13.36.124:808",
    "http://36.99.207.91:808",
    "http://14.152.39.185:8888",
    "http://110.73.0.239:8123",
    "http://221.229.44.94:808",
    "http://222.94.144.183:808",
    "http://171.13.37.182:808",
    "http://221.229.46.239:808",
    "http://222.188.92.14:63000",
    "http://114.239.0.129:808",
    "http://114.230.121.97:808",
    "http://119.5.0.26:808",
    "http://60.183.212.85:808",
    "http://183.32.88.68:808",
    "http://183.32.88.247:808",
    "http://114.230.30.84:808",
    "http://123.169.88.97:808",
    "http://123.56.161.24:1080"
]
