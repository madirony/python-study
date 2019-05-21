# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:23:59 2019

@author: Yeon
"""

#리스트
#리스트는 C언어나 java에서 배열이랑 거의 비슷함
#차이점 : int num[10] 다른자료 넣기 불가능 파이썬은 [1,"문자열",리스트,클래스,객체,다넣을 수 있음]
#리스트 생성 및 초기화

#동적으로 데이터를 삽입하기 위해서 빈리스트 만듬
empty_list = []
empty_list = list()
a = [1,2,3,4,5]
b = ["a","b","c"]
c = [1,"a",2,"b",3,"c"]
d = [a,b,c]

print(a)
print(b)
print(c)
print(d)


#파이썬 이터러블 객체 -> 문자열, 리스트 등등....
#인덱싱, 슬라이싱 가능

print(a[0])
print(a[0:2])
print(a[::2])
print(a[-1])

print(a[::])
print(a[::-1])
#리스트 전체 슬라이싱
print(a[::-1])

#고차원 리스트 요소접근방법
print(d[0][3])
