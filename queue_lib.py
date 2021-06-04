# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:11:45 2021

@author: Mukul Kirti Verma
"""
class cq:
  def __init__(self,capacity):
      self.size=0
      self.rear=-1
      self.front=-1
      self.capacity=capacity
      self.q=[None]*capacity
  def enqueue(self,data):
    if (self.rear+1)%self.capacity==self.front:
      print("queue is full")
      return
    if(self.rear==-1 and self.front==-1):
        self.rear+=1
        self.front+=1
    else:
      self.rear=(self.rear+1)%self.capacity
    self.q[self.rear]=data
    self.size+=1
  def dequeue(self):
    if(self.rear==-1 and self.front==-1):
      print("queue is empty")
      return
    x=self.q[self.front]
    self.q[self.front]=None
    self.size-=1
    self.front=(self.front+1)%self.capacity
    if((self.front%self.capacity)==((self.rear+1)%self.capacity)):
      self.rear=-1
      self.front=-1
    return x
  def display(self):
    for i in self.q:
      print(i,end=" ")
  def isEmpty(self):
    if(self.size==0):
      return True
    else:
      return False
  def isFull(self):
    if(((self.rear+1)%self.capacity)==((self.front%self.capacity))):
      return True
    else:
      return False
    