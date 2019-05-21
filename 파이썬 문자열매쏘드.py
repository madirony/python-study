# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = "Hello"
a.find("h")
#리턴 값 : 처음 문자열이 나온 위치
#없을 경우 -1
#find


"/".join("a")
#join
#문자열 이터레블 객체에 사용가능
#"/".join()


#upper & lower

a = a.upper()
a = a.lower()

#replace
# 특정 문자열을 찾아서 원하는 문자열로 변경 시킴
a = a.replace("h","W")
print(a)

#split 중요
empty = "hi hello how are you".split()
print(empty)


#count
#문자열 안에 내가 원하는 문자열이 몇개 들어가 있는지 확인
article = """
Iron Man Hi SuperMan Iron Man
"""
print(article.count("Iron Man"))


#startwith
# 문자열이 뭘로 시작하는지 파악하는 함수

print("apple".startswith("a"))


