from ast import Return
import queue


class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
        
        return True
    
    def enqueue(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return True
        
    def dequeue(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            temp = self.first
            self.first=None
            self.last=None
            return temp.value
        else:
            temp=self.first
            self.first=temp.next
            temp.next=None
        self.length-=1
        return temp.value
    
    def peek(self):
        if self.length is 0:
            return None
        else:
            return self.first.value
        
    
    def print_queue(self):
        temp = self.first
        if temp is None:
            print("No item in Queue.")
        else:
            while temp:
                print(temp.value)
                temp=temp.next