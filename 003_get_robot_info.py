# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:54:22 2020

@author: Ahn Jun Young 
@description : 로봇배제 표준 정보 취득  
"""

import requests 

urls = ["https://www.naver.com/", "https://heigenberg.com/"] # robot 배제 정보 취득 url 
filename = "robots.txt"

for url in urls : 
        file_path = url + filename 
        print(file_path)                #사이트주소/robots.txt
        resp = requests.get(file_path)  #get방식 request 요청
        print(resp.text)                #request 결과값 취득 (= 여기에 로봇배제 표준 나)
        print("\n")



