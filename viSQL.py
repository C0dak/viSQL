#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__  = "Black Viking"
__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

try:
	__version__ = open("version", "r").read().strip()
except:
	__version__ = "0.0.4"

import os
import sys
import time
import argparse

from src import crawler
from src import sqliscan
from src import reverseip

from thirdparty.colorama import init, Fore, Style

class viSQL:
    def __init__(self):
        self.colors = {
            "red":     Fore.RED,
            "cyan":    Fore.CYAN,
            "blue":    Fore.BLUE,
            "green":   Fore.GREEN,
            "white":   Fore.WHITE,
            "yellow":  Fore.YELLOW,
            "magenta": Fore.MAGENTA,
            "bright":  Style.BRIGHT
        }

        self.crawl = crawler.Crawler()

        self.textTypes = {"info": " [INFO] ", "err": "[ERROR] ", None: ''}

        self.sitesFromReverse  = []
        self.sitesFromCrawler  = {}

        parser = argparse.ArgumentParser()
        parser.add_argument('-t', dest="target", help="scan target's server for sqli", type=str, metavar='www.example.com or 54.201.8.55')

        self.target = parser.parse_args().target

        if self.target == None:
        	parser.print_help()
        	sys.exit()

    def vprint(self, text, color, type):
        print self.colors['yellow'] + self.textTypes[type] + self.colors['magenta'] + "["  + time.strftime("%H:%M:%S") + "] " + self.colors[color] + text

    def banner(self):
        print self.colors["bright"] + self.colors["blue"] + """                                                  
	             ,,                                   
	             db   .M\"""bgd   .g8""8q. `7MMF'      
	                 ,MI    "Y .dP'    `YM. MM        
	`7M'   `MF'`7MM  `MMb.     dM'      `MM MM        
	  VA   ,V    MM    `YMMNq. MM        MM MM        
	   VA ,V     MM  .     `MM MM.      ,MP MM      , 
	    VVV      MM  Mb     dM `Mb.    ,dP' MM     ,M 
	     W     .JMML.P"Ybmmd"    `"bmmd"' .JMMmmmmMMM 
	                                 MMb              
	                                  `bood'                                                        
	\t\t\tVersion: %s
	\t\t\thttp://github.com/blackvkng\n"""%(__version__)

    def main(self):
        self.banner()
    	self.vprint("Program started", "green", "info")

    	self.vprint('-' * 35, 'yellow', 'info')
     	self.vprint('Reverse IP lookup started', 'green', 'info')

     	for site in reverseip.find(self.target):
            self.sitesFromReverse.append('http://' + site)
            self.vprint(" " + site, 'cyan', 'info')

        self.vprint('-' * 35, 'yellow', 'info')
     	self.vprint('Crawler started', 'green', 'info')

     	for site in self.sitesFromReverse:
            self.vprint('Crawling --> ' + site, 'yellow', 'info')

            result = self.crawl.crawl(site)

            if result == "connection error":
                self.vprint('Connection error', 'red', 'err')
                continue
            
            if len(result) != 0 and site not in self.sitesFromCrawler.keys():
                self.sitesFromCrawler.update({site: result})
                
            self.vprint("Found %s URL to SQLi scan"%(len(result)), 'cyan', 'info')
        
        self.vprint('-' * 35, 'yellow', 'info')
        self.vprint('SQLi scan started', 'green', 'info')
     	
        for site, links in self.sitesFromCrawler.items():
            self.vprint('Site: ' + site, 'yellow', 'info')

            for link in links:
                result = sqliscan.scan(link)

                if result == True:
                    self.vprint('SQLi vuln! --> ' + link, 'cyan', 'info')
     				
                elif result == "connection error":
                    self.vprint('Connection error', 'red', 'err')

        self.vprint("Program shutting down", "yellow", "info")
if __name__ == '__main__':
    init(autoreset=True)

    visql = viSQL()
    visql.main()
