# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:52:39 2021

@author: S R SOHAN
"""

x = int(input())
y = int(input())
summ = 0

if(x<y):
    for i in range(x,y+1):
        if(i%13!=0):
            summ +=i
    print(summ)

elif(x>y):
    for i in range(y,x+1):
        if(i%13!=0):
            summ +=i
    print(summ)