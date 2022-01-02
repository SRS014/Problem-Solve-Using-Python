# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:17:17 2021

@author: S R SOHAN
"""

i=1
while(i>0):
    x,y = map(int,input().split())
    if(x<=0):
        continue
    summ = 0
    for i in range(x,x+y):
        summ = summ+i
    print(summ)
    i+1