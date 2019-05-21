# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:08:47 2019

@author: Yeon
"""

#if문
a=10
b=5
if a>b:
    print(a)
    
if a<b:
    print(a)
    
# + = / % // >< 다 가능해~ 
# !=
# is 레퍼런스 아이디 비교 (==)    
a = [1,2,3,4,5]
if not 6 in a:
    print(a)
    
#if , elif, else
a= 10
b= 5

if a > b:
    print(a)
elif a < b:
    print(a)
else:
    print(b)

#중요!
    
    
# && || 
if a>b and a<b:
    print(a)
elif a==b or a!=b:
    print(a)
    
    
#if문 여러개는 조건을 여러번 체크
    #if elif else는 ㄴ한번만 체크