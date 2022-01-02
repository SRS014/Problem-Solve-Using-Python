# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:28:12 2021

@author: S R SOHAN
"""

a,b,c = map(float,input().split())


if((a >= (b+c)) or (b >= (a+c)) or (c >= (a+b))):
    print("NAO FORMA TRIANGULO")
elif((a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b))):
    print("TRIANGULO RETANGULO")
elif((a*a > (b*b + c*c)) or (b*b > (a*a + c*c)) or (c*c > (a*a + b*b))):
    print("TRIANGULO OBTUSANGULO")
elif((a*a < (b*b + c*c)) or (b*b < (a*a + c*c)) or (c*c < (a*a + b*b))):
    print("TRIANGULO ACUTANGULO")
elif((a == b) and (a == c)):
    print("TRIANGULO EQUILATERO")
elif((a == b and a != c)  or (a == c and a != b)) or (b == c and b != a):
    print("TRIANGULO ISOSCELES")