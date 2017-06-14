#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import webbrowser
import urllib
from urllib.parse import quote
import re

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = "192.168.224.171" if s.getsockname()[0] != "192.168.224.171" else "localhost" 
s.close()

def mysearch(z):
    s = 'http://go.mail.ru/search?fm=1&q='+quote(z)
    doc = urllib.request.urlopen(s).read().decode('cp1251',errors='ignore')
    o=re.compile('"url":"(.*?)"')
    l=o.findall(doc)
    sp=[]
    for x in l:
        if((x.rfind('youtube')==-1) and(x.rfind('yandex')==-1) and(x.rfind('mail.ru')==-1) and(x.rfind('.jpg')==-1) and(x.rfind('.png')==-1) and(x.rfind('.gif')==-1)):
            sp.append(x)
    sp = dict(zip(sp, sp)).values()
    sp1=[]
    for x in sp: sp1.append(x)
    return sp1

def __ShutDown__():	
	os.system('shutdown -s')
def __YTOpen__():
	webbrowser.open("http://youtube.com")
	return 1
def __VKOpen__():
	webbrowser.open("http://vk.com")
	return 1
def __cinema__():
	try :
		with urllib.request.urlopen("http://"+main.ip+"/api/other.php?desktop") as url:
			data = json.loads(url.read().decode())
	except BaseException:
		print("except")
		return "0"
	else:
		return data["plus"]

	webbrowser.open(mysearch('смотреть+онлайн+фильм+железний человек 1')[1])
	return 1
