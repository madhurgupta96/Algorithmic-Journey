# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:18:51 2020

@author: Madhur Gupta
"""
class queue_implimentation:
    def __init__(self):
        self.q=[]
    def enqueue(self,a):
        self.q.insert(0,a)
    def  dequeue(self):
        return self.q.pop()
    def isEmpty(self):
        return self.q==[]
    def size(self):
        return len(self.q)
func=queue_implimentation()
print(func.size())
func.enqueue(8)
func.enqueue(5)
print(func.q)