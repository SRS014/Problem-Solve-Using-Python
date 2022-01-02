# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:52:14 2021

@author: S R SOHAN
"""
import math

a, b, c = list(map(int, input().split()))

maior = ((a+b+abs(a-b))/2)
result = (maior + c + abs(maior-c))/2
print("%d eh o maior"%result)