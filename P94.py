# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:16:07 2021

@author: S R SOHAN
"""

n = int(input())

cnt = 0
cnt1 = 0
cnt2 = 0
summ = 0

for i in range(n):
    x,y = list(map(str,input().split()))
    
    x = int(x) 
     
    
    if(y == "C"):
        cnt += x
    elif(y == "R"):
        cnt1 += x 
    elif(y == "S"):
        cnt2 += x 
summ = cnt + cnt1 + cnt2
print("Total:", summ,"cobaias") 
print("Total de coelhos:",cnt)
print("Total de ratos:", cnt1)
print("Total de sapos:", cnt2)
print("Percentual de coelhos: %.2lf"%((cnt*100)/summ),"%")
print("Percentual de ratos: %.2lf"%((cnt1*100)/summ),"%")
print("Percentual de sapos: %.2lf"%((cnt2*100)/summ),"%")