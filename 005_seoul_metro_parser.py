# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:59:59 2020

@author: Ahn Jun Young 
@description : 서울메트로 지하철 정보 웹 스크래핑 
"""


import requests 
from bs4 import BeautifulSoup 

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway" 
resp = requests.get(url)
html_src = resp.text 

soup = BeautifulSoup(html_src, 'html.parser') #parser는 html 소스코드 해석기 
print(type(soup))
print("\n")



print(soup.head)
print("\n")
print(soup.body)
print("\n")


print('title 태그요소: ', soup.title)
print('title 태그이름: ', soup.title.name)
print('title 태그문자열: ', soup.title.string)
print("\n")


# 처음 만나는 이미지 태그 찾기 
# find()는 처음 만나는 태그를 하나 찾
first_img = soup.find(name='img')
print(first_img)
print("\n"); 


target_img = soup.find(name='img', attrs={'alt': 'Seoul-Metro-2004-20070722.jpg'})


# 이미지 경로 추출 
target_img_src = target_img.get('src')
print('이미지 파일 경로 :', target_img_src)



# 이미지 요소를 저장하기 
target_img_resp = requests.get('http:'+target_img_src)
out_file_path = "./output/dowload_image.jpg" 

with open(out_file_path, 'wb') as out_file: 
    out_file.write(target_img_resp.content)
    print("이미지 파일 저장 완료")