# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:08:14 2021

@author: S R SOHAN
"""

count = 0
summ = 0
for i in range(6):
    nums = float(input())  
    if(nums>0):
       count += 1     
       summ = summ + nums
       avg = summ/count
print(count, 'valores positivos')
print("%.1f"%avg)