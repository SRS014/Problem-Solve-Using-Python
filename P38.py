# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 10:32:37 2021

@author: S R SOHAN
"""


x,y = list(map(float, input().split()))

if(x == 1):
    xx = (y*4.00)
    print("Total: R$ %.2f"%xx)
    
elif(x == 2):
    x1 = (4.50*y)
    print("Total: R$ %.2f"%x1)
    
elif(x == 3):
    x2 = (5.00*y)
    print("Total: R$ %.2f"%x2)
    
elif(x == 4):
    x3 = (2.00*y)
    print("Total: R$ %.2f"%x3)
    
else:
    x4 = (1.50*y)
    print("Total: R$ %.2f"%x4)
