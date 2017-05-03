#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re

regex = re.compile(r'<center>(.+)</center>')

try:
        r = requests.get('http://1212.ip138.com/ic.asp')
except:
        print 'Error'
r.encoding = r.apparent_encoding
res = regex.search(r.text)
if res:
        print res.group(1) + u'(ip138数据)'
