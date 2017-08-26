#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__  = "Black Viking"
__version__ = "0.0.4"

__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

import urllib2
import useragent

def open(URL):
	request = urllib2.Request(URL, headers=useragent.randomHeader())

	try:
		resp = urllib2.urlopen(request, timeout=6)
		return (resp.read(), resp.url) 
	except:
		return "connection error"