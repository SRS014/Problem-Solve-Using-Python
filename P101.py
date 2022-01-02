# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:11:22 2021

@author: S R SOHAN
"""
i=1

while i > 0:
    x,y = map(int,input().split())
    #i+=1
    if(x <= 0 or y <= 0):
        break
    else:
        summ= 0
        lst = []
        j=0
        if(x<y):
            for j in range(x,y+1):
                summ += j
                print(j, end = " ")       
            print("Sum=%d"%summ)

        elif(x>y):
            for j in range(y,x+1):
                summ += j
                print(j, end = " ")    
            print("Sum=%d"%summ)
    i+=1
   