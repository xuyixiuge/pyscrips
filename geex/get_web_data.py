#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-12-17
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsobj = BeautifulSoup(html.read())
print(bsobj.html.body.h1)