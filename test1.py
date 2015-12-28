#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/12/23'

import urllib2
import urllib

# response=urllib2.urlopen('http://192.168.109.55')
# html=response.read()
# print html

# req=urllib2.Request('http://192.168.109.55')
# response=urllib2.urlopen(req)
# the_page=response.read()
# print the_page
#! /usr/bin/env python
# -*- coding=utf-8 -*-
# @Author pythontab.com
import urllib2
url="http://pythontab.com"
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
req_timeout = 5
req = urllib2.Request(url,None,req_header)
resp = urllib2.urlopen(req,None,req_timeout)
html = resp.read()
print(html)
