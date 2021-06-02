# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:09:59 2021

@author: Mukul Kirti Verma
"""

l=[[[None]*3]*3],
   
class array:
    def __init__(self,size,dtype):
        
        self.l=[None]*size
        self.size=size
        self.dtype=dtype
        self.length=0
        
        
    def __setitem__(self,index,data):
        
        if(index>=self.size):
            print('index out of range')
            return
        if(self.dtype==type(data) or data ==None):
            if(self.l[index]==None):
                self.length+=1
            if(data==None):
                self.length-=1
            self.l[index]=data
            return
        else:
            print("only {} type of data can be inserted".format(self.dtype))       
            return
    def __getitem__(self,index):
        return self.l[index]
    def __iter__(self):
        for i in self.l:
            if(i!=None):
                yield i
    def sort(self):
        k=[]
        m=[]
        for i in self.l:
            if(i!=None):
                k.insert(0,i)
            else:
                m.append(None)
        k.sort()
        self.l=k+m
    def reverse(self):
        k=[]
        m=[]
        for i in self.l:
            if(i!=None):
                k.insert(0,i)
            else:
                m.append(None)
        
        self.l=k+m
    def search(self,data):
        if(data in self.l):
            return True
        else:
            return False
    def __len__(self):
        return self.length

len(arr)
            
    
arr=array(5,int)
arr[0]=1
arr[1]=6
arr[2]=5
arr[2]=7
arr[0]=5
arr[4]=6
arr[0]=None
arr.length


arr.search(8)
arr.reverse()
arr.sort()
for i in arr:
    print(i)
max(arr)
min(arr)
