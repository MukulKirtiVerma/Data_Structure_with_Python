# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:56:33 2021

@author: Mukul Kirti Verma

a) Left Left Case 

T1, T2, T3 and T4 are subtrees.
         z 2                                     y 
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \ 
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2



b) Left Right Case 

     z                               z                           x
    / \                            /   \                        /  \ 
   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
T1   x                          y    T3                    T1  T2 T3  T4
    / \                        / \
  T2   T3                    T1   T2
  
  
c) Right Right Case 

  z-2                                y
 /  \                            /   \ 
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4
     



     
d) Right Left Case 

   z                            z                            x
  / \                          / \                          /  \ 
T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
   x   T4                      T2   y                  T1  T2  T3  T4
  / \                              /  \
T2   T3                           T3   T4




"""

class Node:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None
        self.height=1
class AVL:
    def __init__(self,data):
        self.root=Node(data)
    def insert(self,current,data):
        
        if current==None:
            return Node(data)
        if(current.val>data):
            current.left=self.insert(current.left,data)
            
        elif(current.val<data):
            current.right=self.insert(current.right,data)
        
        
       
        current.height=1+max(self.getHeight(current.left),self.getHeight(current.right))
        balance_fact=self.getBalance(current)
        #left left
        if(balance_fact==2 and current.left.val>data):
            return self.right_rotate(current)
            
            
        #right right
        if(balance_fact==-2 and current.right.val<data):
            return self.left_rotate(current)
            
        #left right 
        if(balance_fact==2 and current.left.val>data):
             current.left=self.left_rotate(current.left)
             return self.right_rotate(current)
        #right left
        if(balance_fact==-2 and current.right.val>data):
            current.right=self.right_rotate(current.right)
            return self.left_rotate(current)
        return current
            
    def left_rotate(self,z):
        y=z.right
        t2=y.left
        
        y.left=z
        z.right=t2
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y

        
    def right_rotate(self,z):
        y=z.left
        T3=y.right
        
        y.right=z
        z.left=T3
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y      
        
    def getBalance(self,current):
        if current==None:
            return 0
    
        return self.getHeight(current.left)-self.getHeight(current.right)
                
        
    def getHeight(self,current):
        
        if current==None:
            return 0
        return current.height
    def preorder(self,current):
        if(current==None):
            return
        self.preorder(current.right)
    
        
        
av=AVL(5)
av.root=av.insert(av.root,3)
av.root=av.insert(av.root,2)
av.root=av.insert(av.root,6)
av.root=av.insert(av.root,8)
av.preorder(av.root)
    
    
    


