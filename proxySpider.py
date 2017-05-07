#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib
def send_req(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    host='www.youdaili.net'
    req=urllib2.Request(url)
#    req.get_method=lambda: 'HEAD'
    req.add_header('Host',host)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0')
    req.add_header('Upgrade-Insecure-Requests','1')
    res=opener.open(req)
    print cookie
    msg=res.msg
    print msg
    data=res.read()
    print data
    print type(data)
    #print data
url='http://www.youdaili.net/Daili/http/index.html'
if __name__=="__main__":
#        socket.setdefaulttimeout(2)
        send_req(url)
