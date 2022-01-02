# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 15:02:12 2021

@author: S R SOHAN
"""

x = int(input())
y = int(input())

summ = 0
if (x>y):   
    for i in range(y+1,x):
        if(i%2!=0):
            summ=summ+i         
    print(summ)

else:  
    for i in range(x+1,y):
        if(i%2!=0):
            summ=summ+i       
    print(summ)