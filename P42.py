# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:01:48 2021

@author: S R SOHAN
"""

a,b,c = map(int, input().split())
x,y,z = a,b,c

if((x>y and x>z) and (y<x and y>z ) and (z<x and z<y) ):
    print("{0}\n{1}\n{2}".format(z,y,x))
elif((x>y and x>z) and (z<x and z>y ) and (y<x and y<z) ):
    print("{0}\n{1}\n{2}".format(y,z,x))
elif((y>x and y>z) and (x<y and x>z ) and (z<x and z<y) ):
    print("{0}\n{1}\n{2}".format(z,x,y))
elif((y>x and y>z) and (z<y and z>x ) and (x<y and x<z) ):
    print("{0}\n{1}\n{2}".format(x,z,y))
elif((z>x and z>y) and (x<z and x>y ) and (y<x and y<z) ):
    print("{0}\n{1}\n{2}".format(y,x,z))  
elif((z>x and z>y) and (y>x and y<z ) and (z>x and y>x) ):
    print("{0}\n{1}\n{2}".format(x,y,z))
    
print("\n{0}\n{1}\n{2}".format(a,b,c))

