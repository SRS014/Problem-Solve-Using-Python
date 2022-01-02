# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:11:29 2021

@author: S R SOHAN
"""

x,y = map(int,input().split())
cnt = 0
for i in range(1,y+1):      
    print(i, end = 'x')
    cnt += 1
    if cnt==x:
        print()
        cnt = 0
    