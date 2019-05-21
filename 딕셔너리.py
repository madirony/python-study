# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:36:33 2019

@author: Yeon
"""

#dictionary
#자료형, 자료구조
#키 : 밸류
#"연정흠":"01053222218"
#java 해쉬맵과 동일
#이름, 전화번호 -> 딕셔너리 
# 웹 통신할 때 데이터를 json -> 파이썬에서 딕셔너리랑 생김새 똑같음

dic= {}
dic = dict()
dic = {"a":2,"b":4,"c":6} #키는 인트 문자열만 ... # 밸류는 아무거나 상관없음
print(dic["a"]) #인덱스 넣지말고 키를....
print(dic["b"])
print(dic["c"])

#dictionary에 값을 추가하는 법

dic["d"] = 8

print(dic)

#dictionary
#keys
#반복문에 적용하기 위해서 존재하는 함수
print(dic.keys())
#values
#반복문에 적용하기 위해서 존재하는 함수
print(dic.values())
#items
print(dic.items())