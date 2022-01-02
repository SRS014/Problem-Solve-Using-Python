# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:21:43 2021

@author: S R SOHAN
"""

a = input()
b = input()
c = input()

if(a == "vertebrado"):
    if(b == "ave"):
        if(c == "carnivoro"):
            print("aguia")
        elif (c == "onivoro"):
            print("pomba")
    elif (b == "mamifero"):
        if(c == "onivoro"):
            print("homem")
        elif(c =="herbivoro"):
            print("vaca")

elif(a == "invertebrado"):
    if(b == "inseto"):
        if(c == "hematofago"):
            print("pulga")
        elif (c == "herbivoro"):
            print("lagarta")
    elif (b == "anelideo"):
        if(c == "hematofago"):
            print("sanguessuga")
        elif(c =="onivoro"):
            print("minhoca")
