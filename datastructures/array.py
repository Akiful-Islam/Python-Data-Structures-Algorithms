class Array:
    def __init__(self, ):
        self.data = {}
        self.length = 0
        
    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        item = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return item

array = Array()
array.push(1)
array.push(2)
array.push(3)
print(array.length, array.data)
array.pop()
array.delete(0)
print(array.length, array.data)
