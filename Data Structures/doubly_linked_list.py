class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.previous=None
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head= new_node
        self.tail=new_node
        self.length=1
    
    def append(self, value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def prepend(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head = new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        temp = self.tail  
        self.tail = temp.previous
        self.tail.next = None
        temp.previous=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head=temp.next
        self.head.previous=None
        temp.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail = None
        return temp.value
    
    def get_value(self,index):
        if(index<0 or index>=self.length):
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1, index, -1):
                temp=temp.previous  
        return temp
    
    def set_value(self,value,index):
        temp = self.get_value(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,value,index):
        if(index<0 or index >= self.length):
            return False
        if(index==0):
            return self.prepend
        if(index==self.length):
            return self.append
        new_node = Node(value)
        before = self.get_value(index-1)
        after=before.next
        new_node.next=after
        new_node.previous=before
        before.next=new_node
        after.previous=new_node
        self.length+=1
        return 
    
    def remove(self, index):
        if(index<0 or index >= self.length):
            return None
        if(index==0):
            return self.pop_first
        if(index==self.length):
            return self.pop
        temp = self.get_value(index)
        temp.next.previous=temp.previous
        temp.previous.next=temp.next
        temp.next=None
        temp.previous=None
        self.length-=1
        return temp.value
    
    def reverse(self):
        temp = self.head
        before = None
        after = temp.next
        self.head = self.tail
        self.tail = temp
        
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        before = None
        return True
    
    def print_list(self):
        temp = self.head
        if temp is None:
            print("No item in linked list.")
        else:
            while temp:
                print(temp.value)
                temp=temp.next