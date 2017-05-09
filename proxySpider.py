#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib
from lxml import etree
def getHtml(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    host='www.kuaidaili.com'
    req=urllib2.Request(url)
    req.add_header('Host',host)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0')
    req.add_header('Upgrade-Insecure-Requests','1')
    res=opener.open(req)
    data=res.read()
    return data
def parse(data):
    page = etree.HTML(data.decode('utf-8'))
    rows = page.xpath('//div[@id="index_free_list"]/table//tr[td]')
    f = open('proxies.txt', 'a')
    for row in rows:
        #print row.xpath('td[@data-title="IP"]')[0].text+':'+row.xpath('td[@data-title="PORT"]')[0].text
        ip = row.xpath('td[@data-title="IP"]')[0].text
        port = row.xpath('td[@data-title="PORT"]')[0].text
        f.write('%s:%s' % (ip,port))
        f.write('\n')

    f.close()
url='http://www.kuaidaili.com/proxylist/%s/'
if __name__=="__main__":
    file = open('proxies.txt','w')
    file.write('')
    file.close()
    for i in range(1,10):
        parse(getHtml(url % i))
