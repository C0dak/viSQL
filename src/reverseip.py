#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__  = "Black Viking"
__version__ = "0.0.4"

__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

import json
import urllib
import urllib2
import urlparse

import useragent

def find(URL):
    base = urlparse.urlparse(URL).path if urlparse.urlparse(URL).netloc == '' else urlparse.urlparse(URL).netloc

    try:
        request = urllib2.Request('http://domains.yougetsignal.com/domains.php', data=urllib.urlencode({'remoteAddress': base}), headers=useragent.randomHeader())
        source  = json.loads(urllib2.urlopen(request, timeout=5).read())
    except:
        return 'connection error'
    
    domains = [_[0] for _ in source['domainArray']]

    for _ in domains:
    	if 'www.' in _:
    		if _.replace('www.', '') in domains:
    			domains.remove(_)

    return domains