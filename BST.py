

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
           
            return False
        if(current.val==key):
            
            return True
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
    def tree_height(self,current,h=0):
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
            return False
        if(current==None):
            return False
        if(current.val>key):
            if(current.left.val==key):
                
                return current
            else:
               return self.find_parent_node(current.left, key)
        if(current.val<key):
            if(current.right.val==key):
                
                return current
            else:
               return self.find_parent_node(current.right, key)
                
        
        
    def delete(self,current,key):
        if (not self.search(self.root,key)):
            return False
        
        if(self.tree_height(self.root)==1 and current.val==key):
            self.root=None
            return
        if(current.val==key):
            if(current.left==None and current.right==None):
                parent=self.find_parent_node(self.root, key)
                if(parent.val>key):
                    parent.left=None
                    return
                else:
                    parent.right=None
                    return
            if(current.left==None and current.right!=None):
                parent=self.find_parent_node(self.root, key)
                if(parent==False):
                    
                    self.root=current.right
                    
                    return
                if(parent.val>key):
                    parent.left=current.right
                    return
                else:
                    parent.right=current.right
                    return
            if(current.left!=None and current.right==None):
                print(current.val)
                parent=self.find_parent_node(self.root, key)
                
                if(parent==False):
                    
                    self.root=current.left
                   
                    return
                if(parent.val>key):
                    parent.left=current.left
                    return
                else:
                    parent.right=current.left
                    return
                
            if(current.left!=None and current.right!=None):
                mx=self.find_max(current.left)
                self.delete(self.root,mx)
                
                current.val=mx
                return
        if(current.val>key):
            self.delete(current.left,key)
        if(current.val<key):
            self.delete(current.right, key)
        
        
x=BST(5)




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
x.delete(x.root,6.5)

