# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:16:35 2021

@author: S R SOHAN
"""

x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

distance = ((((x2-x1)**2) + ((y2-y1)**2))**(.5))

print("%.4f"%distance)