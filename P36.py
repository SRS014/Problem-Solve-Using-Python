# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 21:00:21 2021

@author: S R SOHAN
"""

import math
a, b, c = list(map(float, input().split()))
d = (b**2)-(4*a*c)

if(a<=0 or d<0):
    print("Impossivel calcular")
else:
    d=math.sqrt(d)    
    r1 = ((-b+d)/(2*a))
    r2 = ((-b-d)/(2*a))
    print("R1 = %0.5f"%r1,"\nR2 = %0.5f"%r2, sep = "")