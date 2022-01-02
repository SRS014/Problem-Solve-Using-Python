# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:21:10 2021

@author: S R SOHAN
"""

count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(5):
    nums = float(input())  
    if nums > 0:
        count3 += 1     
    elif nums < 0:
        count4 += 1  
    if nums%2==0:
        count1 += 1
    elif nums%2!=0:
        count2 += 1    
   
    
           
print(count1, 'valor(es) par(es)')
print(count2, 'valor(es) impar(es)')
print(count3, 'valor(es) positivo(s)')
print(count4, 'valor(es) negativo(s)')