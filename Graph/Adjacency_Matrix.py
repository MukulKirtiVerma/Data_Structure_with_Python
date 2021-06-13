# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:11:38 2021

@author: Mukul Kirti Verma
"""


class graph:
    def __init__(self,v):
        self.v=v
        self.adj_m=[]
        for i in range(v):
            self.adj_m.append([0]*v)
    def insert(self,i,j):
        self.adj_m[i][j]=1
        
    def print_edge(self):
        for i in range(self.v):
            for j in range(self.v):
                if(self.adj_m[i][j]==1):
                    print(i,"--->",j)
    def delete_edge(self,i,j):
        self.adj_m[i][j]=0
    def insert_node(self):
        for i in self.adj_m:
            i.append(0)
        self.adj_m.append([0]*(self.v+1))
        self.v=self.v+1
        
        
g=graph(5)
g.insert(0,1)
g.insert(0,4)
g.insert(1,0)
g.insert(1,2)
g.insert(1,3)
g.insert(1,4)
g.insert(2,1)
g.insert(2,3)
g.insert(3,1)
g.insert(3,2)
g.insert(3,4)
g.insert(4,0)
g.insert(4,1)
g.insert(4,3)


g.insert_node()
g.insert(5,1)

g.delete_edge(4,1)


g.print_edge()


print("graph : ",g.adj_m)
