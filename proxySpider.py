#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib
from lxml import etree
def getHtml(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    host='www.youdaili.net'
    req=urllib2.Request(url)
    req.add_header('Host',host)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0')
    req.add_header('Upgrade-Insecure-Requests','1')
    res=opener.open(req)
    data=res.read()
    return data
def parse(data):
    page = etree.HTML(data.decode('utf-8'))
    hrefs = page.xpath('//ul/li/p/a/@href')
    f = open('proxies.txt', 'w')
    for href in hrefs:
        proxyPage = etree.HTML(getHtml(href).decode('utf-8'))
        proxyList = proxyPage.xpath('//div[@class="content"]/p')
        for proxy in proxyList:
            print proxy.text
            f.write(proxy.text.split('@')[0])
            f.write('\n')

    f.close()
url='http://www.youdaili.net/Daili/http/index.html'
if __name__=="__main__":
    parse(getHtml(url))
