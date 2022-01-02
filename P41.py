# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:38:28 2021

@author: S R SOHAN
"""

a,b = map(float, input().split())

if(a == 0 and b == 0):
    print("Origem")
elif(a == 0):
    print("Eixo Y")
elif(b == 0):
    print("Eixo X")
elif(a>0.0 and b>0.0):
    print("Q1")
elif(a<0.0 and b>0.0):
    print("Q2")
elif(a<0.0 and b<0.0):
    print("Q3")
elif(a>0.0 and b<0.0):
    print("Q4")

    
