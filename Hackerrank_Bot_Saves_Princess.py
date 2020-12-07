# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:46:40 2020

@author: Intel
"""
def displayPathtoPrincess(n,grid):
    me_i=n//2
    me_j=n//2
    for  i in range(n):
        if 'p' in grid[i]:
            pe_i=i
            for j in range(n):
                if 'p'==grid[i][j]:
                    pe_j=j
                    break
            break
    while((me_i!=pe_i) | (me_j!=pe_j)):
        if(me_i-pe_i<0):
            print('DOWN')
            me_i=me_i+1
        elif(me_i-pe_i>0):
            print('UP')
            me_i=me_i-1
        else:
            if(me_j-pe_j>0):
                print('LEFT')
                me_j=me_j-1
            elif(me_j-pe_j<0):
                print('RIGHT')
                me_j=me_j+1
            else:
                break
                
                                
            
            

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)