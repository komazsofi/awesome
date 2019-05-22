# -*- coding: utf-8 -*-


# FIXME: put actual code here
def doStuff():
	print("Do something useful")
	
def addNumbers(a,b):
	assert type(a) != str, "invalid"
	assert type(b) != str, "invalid"
	return(a+b)
	
def wordcount(bookurl):
	import requests
	resp = requests.get(bookurl)
	text=resp.text
	words=text.split()
	return(len(words))