# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:41:53 2021

@author: S R SOHAN
"""

n = int(input())

for i in range(n):
    x,y = map(int, input().split())
    if((x>0 or x<0) and y==0):
        print("divisao impossivel")
        
    else:
        print("%0.1f"%(x/y))
        