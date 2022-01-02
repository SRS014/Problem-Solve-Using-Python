# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:19:27 2021

@author: S R SOHAN
"""

a,b = map(int,input().split())

if(a%b == 0):
    print("Sao Multiplos")

elif(b%a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")