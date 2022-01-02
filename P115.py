# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:35:19 2021

@author: S R SOHAN
"""

i = 1
while(i>0):
    x,y = map(int,input().split())
    if(x==0 or y==0):
        break
    elif(x > 0 and y > 0):
        print("primeiro")
    elif(x < 0 and y > 0):
        print("segundo")
    elif(x < 0 and y < 0):
        print("terceiro")
    elif(x > 0 and y < 0):
        print("quarto")
    i+1