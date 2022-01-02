# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:01:18 2021

@author: S R SOHAN
"""

A,B,C,D = map(float, input().split())

avg = ((A*2+B*3+C*4+D*1)/(10))
print("Media: %.1f"%avg)
if(avg >= 7.0):
    print("Aluno aprovado.")
elif(avg < 5.0):
    print("Aluno reprovado.")
elif(avg >= 5.0 and avg < 7.0):
    print("Aluno em exame.")
    inp = float(input())
    print("Nota do exame: %.1f"%inp)
    avg1 = (avg+inp)/2
    
    if(avg1 >= 5.0):
        print("Aluno aprovado.")
        print("Media final: %.1f"%avg1)
    else:  
        print("Aluno reprovado.")
        print("Media final: %.1f"%avg1)
   


 
