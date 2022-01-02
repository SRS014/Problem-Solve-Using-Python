# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:52:41 2021

@author: S R SOHAN
"""
while True:
    i = 1
    summ = 0
    cnt = 0

    while(cnt<2):
    
        x = float(input())
        
        if(x<0 or x>10):
            print("nota invalida") 
    
        elif (x>=0 and x<=10):
            cnt += 1
            summ += x
        
        i+1
    print("media = %.02f"%(summ/2))
    
    t = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        t= int(input())
        if (t == 1 or t== 2):
            break
    if (t == 2):
        break
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    