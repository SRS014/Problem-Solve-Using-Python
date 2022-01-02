# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:42:26 2021

@author: S R SOHAN
"""

inp = int(input())

for i in range(inp):
    
    x,y = map(int,input().split())
    summ = 0
    
    if(x==y):
        print(0)
    
    elif(x<y):
        for j in range(x+1,y):
            if(j%2 != 0):
                summ = summ + j
        print(summ)
    
    elif(x>y):
        for j in range(y+1,x):
            if(j%2 != 0):
                summ = summ + j
        print(summ)
    