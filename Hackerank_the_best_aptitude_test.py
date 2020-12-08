# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:57:37 2020

@author: Madhur Gupta
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    n=int(input())
    cgpa=input()
    cgpa_lst=cgpa.split(' ')
    indices_c=list(range(n))
    indices_c.sort(key=lambda x: cgpa_lst[x])
    #print(indices_c)
    ap_1=input()
    ap_1_lst=ap_1.split(' ')
    indices_1=list(range(n))
    indices_1.sort(key=lambda x: ap_1_lst[x])
    #print(indices_1)
    ap_2=input()
    ap_2_lst=ap_2.split(' ')
    indices_2=list(range(n))
    indices_2.sort(key=lambda x: ap_2_lst[x])
    ap_3=input()
    ap_3_lst=ap_3.split(' ')
    indices_3=list(range(n))
    indices_3.sort(key=lambda x: ap_3_lst[x])
    ap_4=input()
    ap_4_lst=ap_4.split(' ')
    indices_4=list(range(n))
    indices_4.sort(key=lambda x: ap_4_lst[x])
    ap_5=input()
    ap_5_lst=ap_5.split(' ')
    indices_5=list(range(n))
    indices_5.sort(key=lambda x: ap_5_lst[x])
    m=-1
    flag=0
    diff_1=[]
    for i,j  in zip(indices_c,indices_1):
        diff_1.append(i-j)
    if(diff_1.count(0)>m):
        m=diff_1.count(0)
        flag=1
    diff_2=[]
    for i,j  in zip(indices_c,indices_2):
        diff_2.append(i-j)
    if(diff_2.count(0)>m):
        m=diff_2.count(0)
        flag=2
    diff_3=[]
    for i,j  in zip(indices_c,indices_3):
        diff_3.append(i-j)
    if(diff_3.count(0)>m):
        m=diff_3.count(0)
        flag=3
    diff_4=[]
    for i,j  in zip(indices_c,indices_4):
        diff_4.append(i-j)
    if(diff_4.count(0)>m):
        m=diff_4.count(0)
        flag=4
    diff_5=[]
    for i,j  in zip(indices_c,indices_5):
        diff_5.append(i-j)
    if(diff_5.count(0)>m):
        m=diff_5.count(0)
        flag=5
    print(flag)
        