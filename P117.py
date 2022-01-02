# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:04:12 2021

@author: S R SOHAN
"""


i = 1
summ = 0
cnt = 0
while(i>0):
 
    if cnt == 2:
        break
    x = float(input())
    
    if(x<0 or x>10):
        print("nota invalida") 

    elif (x>=0 and x<=10):
        cnt += 1
        summ += x
    
    i+1
print("media = %.02f"%(summ/2))
 

    



























