# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:05:34 2021

@author: S R SOHAN
"""

n = int(input())
cnt = 0
cnt1 = 0
for i in range(n):
    x = int(input())
    if(x >= 10 and x <= 20):
        cnt = cnt+1
    else:
        cnt1 = cnt1+1
print("%d in"%cnt)
print("%d out"%cnt1)