class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
                
    def isempty(self):
        if self.data==None:
            return True
        return False
    
    def insert(self,data):
        if self.data == None:
            self.data = data
        else:
            node = Node(data)
            self._insert(node)
        self.inorder()
            
    def _insert(self,node):
        if node.data<=self.data:
            if self.left!=None:
                (self.left)._insert(node)
            else:
                self.left=node
        else:
            if self.right!=None:
                (self.right)._insert(node)
            else:
                self.right=node
        
    def inorder(self):
        if self.data==None:
            print("Tree is empty")
        else:
            if self.left!=None:
                (self.left).printTree()
            print(self.data,end=" ")
            if self.right!=None:
                (self.right).printTree()
                
    def preorder(self):
        if self.data==None:
            print("Tree is empty")
        else:
            print(self.data,end=" ")
            if self.left!=None:
                (self.left).printTree()
            if self.right!=None:
                (self.right).printTree()
                
    def postorder(self):
        if self.data==None:
            print("Tree is empty")
        else:
            if self.left!=None:
                (self.left).printTree()
            if self.right!=None:
                (self.right).printTree()
            print(self.data,end=" ")
            
    
    def search(self,value):
        if self.data==None:
            print("tree is empty")
        else:
            self._search(value)
      
    def _search(self,value):
        if self.data==value:
            print("Found")
        else:
            if self.left!=None and value<=self.data:
                (self.left).search(value)
            elif self.right!=None:
                (self.right).search(value)
            else:
                print("Not found")
