# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:26:17 2021

@author: S R SOHAN
"""

i,j = 0,8
for I in range(9):
    
    for jj in range(3):
        II = i+1
        J = j-1
        print("I=%d J=%d"%(II,J))
        if J == 5:
            continue
        j = J
        i = I
