#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__  = "Black Viking"
__version__ = "0.0.4"

__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

import gethtml

import re
import urlparse

class Crawler:
    def __init__(self):
        self.sites = []

    def parameterControl(self, URL):   	
        for site in self.sites:
            if URL.split("=")[0] in site:
                return False

        return True

    def crawl(self, startURL):
        try:
            source, URL = gethtml.open(startURL)
        except:
            return "connection error"

        self.sites = []

        baseURL = 'http://' + '/'.join(URL.split('/')[2:-1]) + '/' if len(URL.split('/')) >= 4 else URL.rstrip('/') + '/'

        for link in re.findall('<a href="(.*?)"', source):
            for _ in ['.php?', '.asp?', '.aspx?', '.jsp?']:
                if _ in link:
                    if link not in self.sites:
                        if self.parameterControl(link) == True:
                            if baseURL.split('/')[2] not in link and 'http' not in link:
                                self.sites.append(baseURL + link.lstrip("/"))                        	
                            else:
                                if baseURL.split('/')[2] in link:
                        	       self.sites.append(link)

        return self.sites