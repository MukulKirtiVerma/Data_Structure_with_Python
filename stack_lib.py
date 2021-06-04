# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:46:24 2021

@author: Mukul Kirti Verma
"""

class stack:
    def __init__(self):
        self.l=[]
        print("empty stack is created successfully")
    def push(self,data):
        self.l.append(data)
        print("element ",data,"is inserted into the stack")
    def pop(self):
        if(len(self.l)==0):
            print("stack is empty, no element to pop")
            return False
        data= self.l.pop()
        print("element ",data,"is poped from the stack")
        return data
    def peek(self):
        return self.l[-1]
    def empty(self):
        if(len(self.l)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.l)
    def top(self,data):
        self.l[-1]=data
    def __len__(self):
        return len(self.l)
    def print_stack(self):
        x=max([len(str(i)) for i in self.l])
        for i in self.l[::-1]:
            print("|"+"\033[4m"+str(i).center(x)+"\033[0m"+"|")
        
