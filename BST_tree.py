# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:57:17 2021

@author: Mukul Kirti Verma
"""

class Node:
    def __init__(self,data):
        self.left=None
        self.val=data
        self.right=None
        
class BST:
    def __init__(self,data):
        self.root=None
        new_node=Node(data)
        self.root=new_node
        self.temp=None
    def insert(self,current,data):
        if(current.val<data):
            if (current.right==None):
                new_node=Node(data)
                current.right=new_node
                return
            else:
                current=current.right
                self.insert(current,data)
        if(current.val>data):
            if (current.left==None):
                new_node=Node(data)
                current.left=new_node
                return
            else:
                current=current.left
                self.insert(current,data)
    def find_min(self,current):
        if current.left==None:
            print(current.val)
            return current.val
        return self.find_min(current.left)
    def find_max(self,current):
        if(current==None):
            return False
        if current.right==None:
            print(current.val)
            return current.val
        return self.find_max(current.right)
    def search(self,current,key):
        if(current==None):
            print("key not found")
            return
        if(current.val==key):
            print("key found")
            return
        if(current.val<key):
            self.search(current.right,key)
        if(current.val>key):
            self.search(current.left,key)
    def inorder(self,current):
        if(current==None):
            return
        self.inorder(current.left)
        print(current.val ,end=" ")
        self.inorder(current.right)  
    def preorder(self,current):
        if(current==None):
            return
        print(current.val ,end=" ")
        self.preorder(current.left)
        self.preorder(current.right)  
    def postorder(self,current):
        if(current==None):
            return
        self.postorder(current.left)
        self.postorder(current.right)      
        print(current.val ,end=" ")
    def tree_height(self,current,h):
        if(current==None):
            return h
        h1=self.tree_height(current.right,h+1)
        h2=self.tree_height(current.left,h+1)
        return max(h1,h2)
    def print_level(self,current,l):
        if(current==None):
            return
        if(l==0):
            print(current.val)
            return
        if l>0:
            self.print_level(current.left,l-1)
            self.print_level(current.right,l-1)
    def BFS(self,current):
        h=self.tree_height(self.root, 0)
        print(h)
        for i in range(h):
            self.print_level(self.root,i)
    
    def find_parent_node(self,current,key):
        if(self.root.val==key):
           self.current=False
           self.pos='_'
           
        if(current==None):
            return
        if(current.right):
            if(current.right.val==key):
                self.current=current
                self.pos='right'
            
        if(current.left):
            if(current.left.val==key):
                self.current=current
                self.pos='left'
            
        if(current.val>key):
            self.find_parent_node(current.left,key)
        if(current.val<key):
            self.find_parent_node(current.right,key)
        return self.current,self.pos
            
        
        
    def delete(self,current,key):
        if(current==None):
            print("No key found")
            return
        if(self.tree_height(self.root,0)==1 and current.val==key):
            self.root=None
            return
        if(current.val==key):
            if(current.left==None and current.right==None):
                  
                    x,p=self.find_parent_node(self.root,key)
                    print(p)
                    if(p=='left'):
                        x.left=None
                        return
                    elif(p=='right'):
                        
                        x.right=None
                        return
            if(current.left==None and current.right!=None):
            
                x,p=self.find_parent_node(self.root,key)
                if(p=='left'):
                        x.left=current.right
                        return
                elif(p=='right'):
                        x.right=current.right
                        return
                else:
                    mx=self.find_max(current.left)
                    if(mx==False):
                        mx=self.find_min(current.right)
                        print(mx)
                        self.delete(self.root,mx)
                    else:
                        self.delete(self.root,mx)
                    current.val=mx
                    return
                    
            if(current.left!=None and current.right==None):
                x,p=self.find_parent_node(self.root,key)
                if(p=='left'):
                        x.left=current.left
                        return
                elif(p=='right'):
                        x.right=current.left
                        return
                else:
                    mx=self.find_max(current.left)
                    if(mx==False):
                        mx=self.find_max(current.right)
                        self.delete(self.root,mx)
                    else:
                        self.delete(self.root,mx)
                    current.val=mx
                    return
            if(current.left!=None and current.right!=None):
                mx=self.find_max(current.left)
                if(mx==False):
                    mx=self.find_max(current.right)
                    self.delete(self.root,mx)
                else:
                    self.delete(self.root,mx)
                current.val=mx
                return
        
        if(current.val>key):
            self.delete(current.left,key)
        if(current.val<key):
            self.delete(current.right,key)
x=BST(2)


"""

x.insert(x.root,7)
x.insert(x.root,2)
x.insert(x.root,4)
x.insert(x.root,6)
x.insert(x.root,0)
x.find_min(x.root)
x.find_max(x.root.left)
x.search(x.root,6)
x.inorder(x.root)
x.preorder(x.root)
x.postorder(x.root)
x.tree_height(x.root, 0)
x.BFS(x.root)

"""