# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:40:32 2021

@author: S R SOHAN
"""

n = int(input())

for i in range(n):
    x1,x2,x3 =list(map(float, input().split())) 
    avg1 = (x1*2+x2*3+x3*5)/10
    print("%.1f"%avg1)