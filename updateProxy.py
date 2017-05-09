#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib
import json
def getHtml(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    req=urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0')
    req.add_header('Upgrade-Insecure-Requests','1')
    res=opener.open(req)
    data=res.read()
    return data
url='http://www.xdaili.cn/ipagent//freeip/getFreeIps?page=1&rows=10'
if __name__=="__main__":
    file = open('proxies.txt','w')
    data = json.loads(getHtml(url))
    for proxy in data['rows']:
        file.write('%s:%s' % (proxy['ip'],proxy['port']))
        file.write('\n')
    file.close()

