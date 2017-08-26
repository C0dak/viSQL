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
import urllib2
import urlparse

def find(URL):
    base = urlparse.urlparse(URL).path if urlparse.urlparse(URL).netloc == '' else urlparse.urlparse(URL).netloc

    try:
        source, URL = gethtml.open("http://viewdns.info/reverseip/?host=%s&t=1"%(base))
    except:
        return "connection error"
	
    return re.findall("<td>(.*?)</td>", source)[3:]
