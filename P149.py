# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:42:24 2021

@author: S R SOHAN
"""

summ = 0
i = 1

while(i>0):
    
    a,n = map(int,input().split())
    if n<0:
        continue
    for i in range(a,(a+n)):
        summ = summ+i
    print(summ)
    