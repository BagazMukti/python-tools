#!/usr/bin/env python
# Coded by Bagaz

from urllib2 import Request, urlopen, URLError, HTTPError

def find():
	login = open("login.txt","r");
	link = raw_input("Input target: ")
	print "\n\nResult: \n"
	while True:
		sub_link = login.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print " => ",req_link

def banner():
	print "\n[~] AdminFinder v1 [~]\n\n Coded by Bagaz (http://www.facebook.com/bacotgoblok)\n\n  Don't use http\n\n Greetz: My Friends\n"

banner()
find()

exit