# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:07:41 2019

@author: Yeon
"""

def hanoiStack(ndisks, startPeg=1, endPeg=3):
    stack = []
    stack.append((ndisks, startPeg, endPeg, False))
    while len(stack) > 0:
        disks, start, end, move = stack.pop()
        extraPeg = 6 - end - start
        if move:
            print(start, "번 기둥의", disks, "번 원반을", end, "번 기둥에 옮긴다.")
        elif disks > 0:
            stack.append((disks - 1, extraPeg, end, False))
            stack.append((disks, start, end, True))
            stack.append((disks - 1, start, extraPeg, False))

hano = hanoiStack(int(input("몇개의 원판..")))