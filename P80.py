# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:49:22 2021

@author: S R SOHAN
"""
lst = []
for i in range(100):
    n = int(input())
    lst.append(n)
    maxposi = lst.index(max(lst))        
    
print(max(lst))
print(maxposi+1) 