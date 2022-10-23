class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class SinglyLinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
        
    def append(self, value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
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
            self.head = new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        before = self.head            
        while (temp.next):
            before=temp
            temp=temp.next
        self.tail = before
        self.tail.next = None
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
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail = None
        return temp.value
    
    def set_value(self,value,index):
        temp = self.__get_node(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def get_value(self,index):
        temp = self.__get_node(index)
        if temp:
            return temp.value
        return None
    
    def __get_node(self,index):
        if(index<0 or index>=self.length):
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def insert(self,value,index):
        if(index<0 or index > self.length):
            return False
        if(index==0):
            return self.prepend
        if(index==self.length):
            return self.append
        new_node = Node(value)
        temp = self.__get_node(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return 
    
    def remove(self, index):
        if(index<0 or index > self.length):
            return None
        if(index==0):
            return self.pop_first
        if(index==self.length):
            return self.pop
        before = self.__get_node(index-1)
        temp = before.next
        before.next=temp.next
        temp.next=None
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
          
        
new_linked_list = SinglyLinkedList(5)
new_linked_list.append(10)
new_linked_list.prepend(12)
new_linked_list.append(1)
new_linked_list.print_list()

new_linked_list.reverse()
new_linked_list.print_list()

        