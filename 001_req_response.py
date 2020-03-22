# -*- coding: utf-8 -*-


"""
Created on Sun Mar 22 16:31:56 2020

@author: Ahn Jun Young 
@description : 특정 웹사이트에 request 보내고 response 값 출력 
"""
import requests 


# 1. 요청 url 세팅 
url = "https://www.python.org/"  # 파이썬 사이트 
url_atone = "https://ct-auth.a-to-ne.jp/v1/atone.js" #pg사 atone 테스트서버 

# 2. 실제 request 
resp = requests.get(url)
resp_atone = requests.get(url_atone)

# 3. request 결과값 취득 
print(resp)
print(resp_atone)

