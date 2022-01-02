# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:10:05 2021

@author: S R SOHAN
"""

a, b, c, d = list(map(int, input().split()))

if((b>c and d>a) and ((c+d)>(a+b)) and (c>0 and d>0) and (a%2==0)):
    print("Valores aceitos")
    
else:
    print("Valores nao aceitos")
    