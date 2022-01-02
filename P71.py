# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:18:57 2021

@author: S R SOHAN
"""

x = int(input())
y = int(input())

summ=0
summ1 = 0
summ2 = 0
if x > 0 and y>0 and(x==y):   
    for i in range(x,y):
        if(i%2!=0):
            summ=summ+i
            print(i)
    print(summ)

if x > 0 and y>0 and(x<y):   
    for i in range(x,y):
        if(i%2!=0):
            summ=summ+i
            print(i)
    print(summ)
    
elif x > 0 and y>0 and(x>y):   
    for i in range(y,x):
        if(i%2!=0):
            summ=summ+i
            print(i)
    print(summ)

elif x < 0 and y>0:   
    for i in range(x,y):
        if(i%2!=0):
            summ=summ+i
            print(i)
    print(summ)

elif x > 0 and y < 0:   
    for i in range(y+1,x):
        if(i%2!=0):
            summ=summ +i
            print(i)
    print(summ)

elif x < 0 and y < 0:   
    for i in range(x,y):
        if(i%2!=0):
            summ=summ+i
            print(i)
    print(summ)