# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:23:04 2021

@author: S R SOHAN
"""

i = 1
cnt = 0
cnt1 = 0
cnt2 = 0


while i>0:
    
    n = int(input())
    
    if(n==1):
        cnt +=1
    elif(n==2):
        cnt1 +=1     
    elif(n==3):
        cnt2 +=1 
    elif(n==4):
        break
    
    i+1
print("MUITO OBRIGADO")
print("Alcool: %d"%cnt)        
print("Gasolina: %d"%cnt1) 
print("Diesel: %d"%cnt2) 
    