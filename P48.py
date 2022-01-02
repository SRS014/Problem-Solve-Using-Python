# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 21:39:18 2021

@author: S R SOHAN
"""

a = float(input())

if(a >= 0.00 and a <= 400.00):
    sal = (a*.15+a)
    per = (a*.15)
    print("Novo salario: %.2f"%sal)
    print("Reajuste ganho: %.2f"%per)
    print("Em percentual: 15 %")
    
elif(a >= 400.01 and a <= 800.00):
    sal = (a*.12+a)
    per = (a*.12)
    print("Novo salario: %.2f"%sal)
    print("Reajuste ganho: %.2f"%per)
    print("Em percentual: 12 %")
    
elif(a >= 800.01 and a <= 1200.00):
    sal = (a*.10+a)
    per = (a*.10)
    print("Novo salario: %.2f"%sal)
    print("Reajuste ganho: %.2f"%per)
    print("Em percentual: 10 %")


elif(a >= 1200.01 and a <= 2000.00):
    sal = (a*.07+a)
    per = (a*.07)
    print("Novo salario: %.2f"%sal)
    print("Reajuste ganho: %.2f"%per)
    print("Em percentual: 7 %")
    
elif(a >= 2000.00):
    sal = (a*.04+a)
    per = (a*.04)
    print("Novo salario: %.2f"%sal)
    print("Reajuste ganho: %.2f"%per)
    print("Em percentual: 4 %")