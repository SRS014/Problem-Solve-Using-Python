# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:52:10 2021

@author: S R SOHAN
"""

inp = int(input())

year = inp // 365
month = inp % 365
month1 = month // 30
day = month % 30


print("%d ano(s)"%year, "\n%d mes(es)"%month1, "\n%d dia(s)"%day, sep="" )