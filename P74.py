# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:12:19 2021

@author: S R SOHAN
"""

n = int(input())

for i in range(n):
    x = int(input())
    if(x%2 == 0 and x >0):
        x1 = x
        print("EVEN POSITIVE")
    elif(x%2 !=0 and x>0):
        print("ODD POSITIVE")
    elif(x%2 ==0 and x<0):
        print("EVEN NEGATIVE")
    elif(x%2 !=0 and x<0):
        print("ODD NEGATIVE")
    elif(x == 0 ):
        print("NULL")

