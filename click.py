#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib
import socket
import base64


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
    i = 0
    proxies = open('proxies.txt','rU')
    for proxy in proxies.readlines():
        p = {"http":"%s" % proxy.strip('\n')}
        print p
        print i
        try:
            proxy_s=urllib2.ProxyHandler(p)
            opener=urllib2.build_opener(proxy_s)
            req = urllib2.Request(url, data, headers)
            response = opener.open(req)
            result = response.read()
            print result
            if result == 'error':
                break
            if result == 'ok':
                i = i+1
            if i >= 5:
                break
        except Exception,e:
            continue
    proxies.close()
def parseParam(str):
    param = dict()
    for kv in str.split('&'):
        param[kv.split('=')[0]] = kv.split('=')[1]
    return param
def simulateLongDanClick(plainUrl):
    print plainUrl
    headers = getCommonHeader();
    headers['Referer'] = plainUrl
    decodeData = base64.b64decode(plainUrl.split('?')[1].split('=')[1])
    param = parseParam(decodeData)
    url = "http://cn.battleofballs.com/share?type=3&id=%s" % param['id']
    data = None
    #simulateBbtClick(param['id'], param['Account'])
    i = 0
    proxies = open('proxies.txt','rU')
    for proxy in proxies.readlines():
        p = {"http":"%s" % proxy.strip('\n')}
        print i
        try:
            proxy_s=urllib2.ProxyHandler(p)
            opener=urllib2.build_opener(proxy_s)
            req = urllib2.Request(url, data, headers)
            response = opener.open(req)
            result = response.read()
            print result
            if result == 'ok':
                i = i+1
            if i >= 30:
                break
        except Exception,e:
            continue
    proxies.close()


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
    if plainUrl.find('b=') <> -1:
        simulateLongDanClick(plainUrl)

def start():
    file = open('link.txt','r')
    for link in file.readlines():
        handleUrl(link)
    file.close()
#url='http://t.cn/RJhm9Mw'
if __name__=="__main__":
    socket.setdefaulttimeout(15)
    start();
