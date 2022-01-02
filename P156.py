# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:50:08 2021

@author: S R SOHAN
"""


n = 0.0

for i in range(1,40):      
    #j = i-1
    n += ((i+2)/(i*2))
    print(i+2,i*2)
print("%.2f"%n) 