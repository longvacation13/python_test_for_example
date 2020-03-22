# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:37:19 2020

@author: Ahn Jun Young 
@description : 웹사이트 get 요청을 보내고 응답 객체를 받음 
"""

import requests 

url = "https://heigenberg.com"     #소스코드 확인할 url 
resp = requests.get(url)           #get 방식 requests 

html = resp.text                   # 소스코드 저장변수 
print(html)                        # 응답객체 출력 


