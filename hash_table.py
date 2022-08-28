class HashTable:
    def __init__(self, size=5):
        self.data_map=[None]*size
    
    def __hash(self, key):
        hash_value=0
        for letter in key:
            hash_value=(hash_value+ord(letter)*17)%len(self.data_map)
            return hash_value
        
    def set_item(self, key, value):
        index= self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get_item(self, key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None
    
    def get_keys(self):
        keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys
        
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i ,": ", val)
            
hash_table = HashTable()

hash_table.set_item('tausif',232)
hash_table.set_item('rafi',323)
hash_table.set_item('monabbir',123)
hash_table.set_item('tabjir',321)

print(hash_table.get_keys())

hash_table.print_table()

print(hash_table.get_item('tausif'))
print(hash_table.get_item('monabbir'))