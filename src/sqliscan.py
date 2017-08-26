#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__  = "Black Viking"
__version__ = "0.0.4"

__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

import gethtml
import urllib2

sql_errors = [
	'Fatal error', 
	'mysql_fetch', 
	'Query failed', 
	'Error:unknown', 
	'mysql_num_rows',
	'error in your SQL syntax', 
	'Syntax errormysql_num_rows', 
	"Microsoft JET Database Engine error '80040e14'", 
	'supplied argument is not a valid MySQL result resource in'
	]


def scan(URL):
    try:
        source, URL = gethtml.open(URL + '\'')
    except:
        return "connection error"

    for err in sql_errors:
        if err in source:
            return True

    return False
