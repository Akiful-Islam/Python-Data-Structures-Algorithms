class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
        return True
    
    def push(self,value):
        new_node=Node(value)
        if self.height is 0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return True
        
    def pop(self):
        if self.height is 0:
            return None
        elif self.height is 1:
            temp = self.top
            self.top=None
            return temp.value
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        self.height-=0
        return temp.value
    
    def peek(self):
        if self.height is 0:
            return None
        else:
            return self.top.value
        

    def print_stack(self):
        temp = self.top
        if temp is None:
            print("No item in Stack.")
        else:
            while temp:
                print(temp.value)
                temp=temp.next
    
    