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
    __start_urls = []
    __domains = []
    __dataLink = []
    def __init__(self):
        for i in range(1, 2046):
            self.__start_urls.append('')

