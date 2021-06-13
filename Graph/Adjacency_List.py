# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 15:55:27 2021

@author: Mukul Kirti Verma
"""
class graph:
    def __init__(self):
        self.adj_l={}
    def insert_edge(self,i,j):
        if(i in self.adj_l.keys()):
            self.adj_l[i].append(j)
        else:
            self.adj_l[i]=[j]
    def delete_edge(self,i,j):
        self.adj_l[i].remove(j)
        self.adj_l[j].remove(i)
    
    def print_graph(self):
      for node in self.adj_l.keys():
        s=str(node)
        for edge in self.adj_l[node]:
          s+=str("-->"+str(edge))
        print(s)
                
                    
g=graph()
g.insert_edge(0,1)
g.insert_edge(0,2)
g.insert_edge(1,0)
g.insert_edge(1,3)
g.insert_edge(1,4)
g.insert_edge(2,0)
g.insert_edge(2,4)
g.insert_edge(3,1)
g.insert_edge(3,4)
g.insert_edge(3,5)
g.insert_edge(4,1)
g.insert_edge(4,2)
g.insert_edge(4,3)
g.insert_edge(4,5)  
g.insert_edge(5,3)
g.insert_edge(5,4)

g.print_graph()      

g.delete_edge(0,1)

