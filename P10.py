# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:57:42 2021

@author: S R SOHAN
"""

p1, p2, p3 = list(map(float, input().split()))
q1, q2, q3 = list(map(float, input().split()))

p_tot = p2*p3
q_tot = q2*q3
Total = p_tot + q_tot
print("VALOR A PAGAR: R$ %.2f"%Total)

#arr = list(map(int, input().split()))
