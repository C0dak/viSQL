#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"

import os

content = """\
#!/bin/bash

cd /usr/share/visql
python2 viSQL.py "$@" """

def main():
	if os.name != "nt":
		if os.getuid() == 0:
			if os.path.exists('/usr/share/visql') == True:
				os.system('rm -rf /usr/share/visql /usr/bin/visql')

			os.system("git clone http://github.com/blackvkng/viSQL.git /usr/share/visql")

			file = open("/usr/bin/visql", "w")
			file.write(content)
			file.close()
			
			os.system("chmod +x /usr/bin/visql")

			print "\n[+] Installation finished, type 'visql' to use program!"
		else:
			print "Run as root!"
	else:
		print "This script doesn't work on Windows!"

if __name__ == "__main__":
	main()
