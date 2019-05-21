# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:22:45 2019

@author: Yeon
"""

#객체 -> 메소드 사용시 "."으로 접근

a=[]
#append
a.append(1)
a.append(2)
a.append(3)

#extend
a.extend([4,5,6])
print(a)
b=[7,8,9]
a= a+b #[1.......9] extend는 오류가 안나오고 +는 오류가 나옴 오류검출하고 싶을때 + 씀
print(a)

#reverse
a.reverse()
print(a)

#sort
c = [8,6,4,5,3,1,2,9,7]
c.sort(reverse=True) #reverse=True를 넣으면 내림차순 sort 라는건 False라는 인자가 디폴트
print(c)

#remove
d = [1,2,3,4,5,6,7,8,9]
d.remove(1) #인자는 값 인덱스 아님
print(d)


#insert 자료구조만들때 필요
#append -> 맨뒤에 추가
#장점 : insert는 원하는 위치에 자료를 추가
#주로 맨앞에 값을 넣고 싶을 때 사용
d.insert(5,100)
print(d)


#pop
#도 역시 자료구조 만들때 사용
#리스트 섞는 함수 -> 값하나 뽑을 때 외에는 잘 사용x
d.pop()
print(d)