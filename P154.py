# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:02:04 2021

@author: S R SOHAN
"""

i = 1
cnt = 0
summ = 0 
while(i>0):
    
    n = int(input())
    if n < 0:
        break
    cnt = cnt+1
    summ = summ + n
avg = summ/cnt
print("%.2f"%avg)