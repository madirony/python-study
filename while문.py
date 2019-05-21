# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:23:14 2019

@author: Yeon
"""

#while문->반복문
#일을 반복적으로 실행해야 할때에 사용

a=1 #1씩 증가시키는 a
b=10

#while a<=b:
#    print(a)
    #a++는 존재하지 않음
#    a +=1
    
#무한루프 탈출법
while True:
    print(a)
    a += 1
    #escape문을 넣어줘야
    if a == 10:
        break
    

