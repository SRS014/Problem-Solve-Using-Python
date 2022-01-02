# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:28:51 2021

@author: S R SOHAN
"""
pi = 3.14159
A, B, C = list(map(float, input().split()))

Ar_rectangled_triangle = (.5*A*C)
Ar_radius_Circle = (pi*C*C)
Ar_trapezium = (((A+B)/2)*C)
Ar_square = (B*B)
Ar_rectangle = (A*B)

print("TRIANGULO: %.3f"%Ar_rectangled_triangle)
print("CIRCULO: %.3f"%Ar_radius_Circle)
print("TRAPEZIO: %.3f"%Ar_trapezium)
print("QUADRADO: %.3f"%Ar_square)
print("RETANGULO: %.3f"%Ar_rectangle)