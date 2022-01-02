# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:16:37 2021

@author: S R SOHAN
"""

i = 1
while(i>0):
    x,y = map(int,input().split())
    
    if(x==y):
        break
    elif (x>y):
        print("Decrescente")
    elif(x<y):
        print("Crescente")
        