# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:31:09 2020

@author: Madhur Gupta
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m=input()
n=int(n_m.split(' ')[0])
m=int(n_m.split(' ')[1])
o=input()
o1=o.split(' ')
a=input()
a1=a.split(' ')
b=input()
b1=b.split(' ')
h=0
a2=set(a1)
b2=set(b1)
#o2=set(o1)
for i in o1:
    if i in a2:
        h=h+1
    elif i in b2:
        h=h-1
    else:
        pass
print(h)        

