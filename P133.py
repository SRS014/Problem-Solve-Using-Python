# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:06:23 2021

@author: S R SOHAN
"""

x = int(input())
y = int(input())

if(x<y):
    for i in range(x+1,y):
        if(i%5==2 or i%5==3 ):  
            print(i)
elif(x>y):
    for i in range(y+1,x):
        if(i%5==2 or i%5==3 ):  
            print(i)
