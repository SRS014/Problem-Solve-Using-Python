# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 09:53:06 2021

@author: S R SOHAN
"""



a = float(input())

if(a >= 0.00 and a <= 2000.00):
    print("Isento")
else:
     
    if(a >= 2000.01 and a <= 3000.00):          
        aa = a-2000.00
        tot = aa*.08
        print("R$ %.2f"%tot)

    elif(a >= 3000.01 and a <= 4500.00):
        aa = a-2000.00
        aaa = aa - 1000
        tot = 1000*.08+aaa*.18
        print("R$ %.2f"%tot)   

    elif(a > 4500.00):
        aa = a-2000.00
        aaa = aa - 1000
        a4 = aaa-1500
        tot = 1000*.08+1500*.18 + a4*.28
        print("R$ %.2f"%tot) 
