#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, json 
import functions as f
import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = "192.168.224.171" if s.getsockname()[0] != "192.168.224.171" else "localhost" 
s.close()

text_to_func = {
		"1" : f.__ShutDown__,
		"2" : f.__YTOpen__,
		"3" : f.__VKOpen__,
		"4" : f.__cinema__
}

def check():
	try :
		with urllib.request.urlopen("http://"+ip+"/api/other.php?desktop") as url:
			data = json.loads(url.read().decode())
	except BaseException:
		print("except")
		return "0"
	else:
		return data["do"]

def update():
	do = check()
	print('---')
	if do != "0" : 
		text_to_func[do]()
		urllib.request.urlopen("http://"+ip+"/api/other.php?desktop=done")
	u = threading.Timer(1.0,update)
	u.start()
        
#update()
f.__cinema__()