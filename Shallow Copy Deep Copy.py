# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:17:27 2019

@author: Yeon
"""

a= [1,2,3,4,5]
b=a
b[0] = 10

#결과가 같음 C언어에선 포인터 같은거
#레퍼런스 아이디가 똑같아지는 것
print(a)
print(b)
#b만 건들였는데 a도 같이 바뀜
#Shallow Copy 


#진짜 중요함 까먹지 말구

#DEEP COPY
a =[1,2,3,4,5]
b= a[:] #객체의 id가 아니라 값일 경우 DEEP COPY
b[0]=10
print(a)
print(b)

