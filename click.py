#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib

def getCommonHeader():
    return {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "DNT":"1",
        "Host":"cn.battleofballs.com",
        "Origin":"http://www.battleofballs.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0"
    }


def simulateBbtClick(id,account):
    headers = getCommonHeader();
    headers['Referer'] = "http://www.battleofballs.com/index_PC.html?id=%s&Account=%s" % (id,account)
    url = "http://cn.battleofballs.com/share?type=1&id=%s" % id
    data = None
    proxies={"http":"43.241.227.180:8000"}
    proxy_s=urllib2.ProxyHandler(proxies)
    opener=urllib2.build_opener(proxy_s)
    req = urllib2.Request(url, data, headers)
    response = opener.open(req)
    print response.read()

def handleUrl(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0')
    req.add_header('Upgrade-Insecure-Requests','1')
    res = opener.open(req)
    plainUrl = res.geturl()
    #print data
    if plainUrl.find("Account") <> -1:
        params = plainUrl.split('?')[1]
        id = params.split('&')[0].split('=')[1]
        account = params.split('&')[1].split('=')[1]
        print id
        print account
        simulateBbtClick(id,account)

def start():
    file = open('link.txt','r')
    for link in file.readlines():
        handleUrl(link)
#url='http://t.cn/RJhm9Mw'
if __name__=="__main__":
#        socket.setdefaulttimeout(2)
    start();
