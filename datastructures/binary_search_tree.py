class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self, value):
        new_node=Node(value)
        self.root=new_node
        
    def insert(self, value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if(new_node.value==temp.value):
                return False
            if(new_node.value<temp.value):
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    
    def remove(self, value):
        if self.root is None:
            return False
        temp=self.root
        parent=None
        while(temp):
            if(value<temp.value):
                parent=temp
                temp=temp.left
            elif(value>temp.value):
                parent=temp
                temp=temp.right
            else:
                if temp.left is None:
                    if parent is None:
                        self.root=temp.right
                    else:
                        if temp.value<parent.value:
                            parent.left=temp.right
                        elif temp.value>parent.value:
                            parent.right=temp.right
                elif temp.right is None:
                    if parent is None:
                        self.root=temp.left
                    else:
                        if temp.value<parent.value:
                            parent.left=temp.left
                        elif temp.value>parent.value:
                            parent.right=temp.left
                else:
                    parent_of_rightmost=temp
                    rightmost=temp.right
                    while(rightmost.left):
                        parent_of_rightmost=rightmost
                        rightmost=rightmost.left
                    temp.value=rightmost.value
                    if parent_of_rightmost.right==rightmost:
                        parent_of_rightmost.right=rightmost.right
                    else:
                        parent_of_rightmost.left=rightmost.right
                return True
        return False
                
    def exists(self,value):
        temp=self.root
        while(temp):
            if(value<temp.value):
                temp=temp.left
            elif(value>temp.value):
                temp=temp.right
            else:
                return True
        return False
    
    def breadth_first_traversal(self):
        if self.root is None:
            return []
        queue=[self.root]
        result=[]
        while(queue):
            temp=queue.pop(0)
            result.append(temp.value)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return result
    
    def depth_first_traversal_inorder(self):
        result=[]
        def traverse(node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return result
    
    def depth_first_traversal_preorder(self):
        result=[]
        def traverse(node):
            result.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return result
    
    def depth_first_traversal_postorder(self):
        result=[]
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.value)
        traverse(self.root)
        return result

tree = BinarySearchTree(10)

tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(12)
tree.insert(8)
tree.insert(20)
    
print(tree.breadth_first_traversal())
print(tree.depth_first_traversal_inorder())
print(tree.depth_first_traversal_preorder())
print(tree.depth_first_traversal_postorder())

tree.remove(10)
tree.remove(1)
tree.remove(20)

print(tree.breadth_first_traversal())
print(tree.depth_first_traversal_inorder())
print(tree.depth_first_traversal_preorder())
print(tree.depth_first_traversal_postorder())
