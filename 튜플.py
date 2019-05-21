# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:46:44 2019

@author: Yeon
"""

#tuple
#생김새가 리스트랑 똑같음
#저장되는 방식도 똑같고 이터러블 객체 -> 슬라이싱, 인덱싱
#immutable한 객체 == 오염이 안되는 객체
#데이터 분석 -> 샘플들을 받았음 -> 튜플 사용하면 오염 x
#절대 값을 바꿀 수 없음

tuple1 = ()
#type casting
#tuple()
list()
dict()
str()
int()

tuple2 = tuple()
tuple3 = (1,2,3)

# immutable하다 == 레퍼런스 아이디가 지속적으로 같아야 한다.
#(1,2,3) -> (1,2,3,4) 튜플안에 리스트가 있으면 바꿀 수 있음
# a= a.replace() -> 레퍼런스 아이디가 변경됨
# a.append(1) -> 레퍼런스 아이디가 변경이 안됨
#append 함수 기억기억

b = (1,2,3,["Hi","hello"])
b[3].append("babo")


print(b)