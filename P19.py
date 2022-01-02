# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:37:12 2021

@author: S R SOHAN
"""

inp = int(input())

hours = inp // 3600
mints = inp // 60
mints1 = mints % 60
seconds = inp % 60
print("%d:"%hours, "%d:"%mints1, "%d"%seconds, sep="" )
