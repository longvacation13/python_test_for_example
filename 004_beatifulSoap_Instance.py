# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:40:04 2020

@author: Ahn Jun Young 
@description : BeautifulSoup 객체 만들기 
"""

# html 소스코드 해석 : parsing이라고 부름 
# 가상환경에서 not installed 클릭 후 beautifulsoup4 검색 
# 안나올 경우 update channel, update index 이후 재검색 


# 1. 지하철 정보 취득 ( 로봇배제 표준 ) 
import requests 

urls = ["https://en.wikipedia.org/"]
file_name = "robots.txt" 

for url in urls :
    file_path = url+file_name
    print(file_path)
    
    # request 
    resp1 = requests.get(file_path)
    print(resp1.text) # 로봇배제 표준 출력 
    
    

