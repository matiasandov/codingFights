class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
            return True
        
        temp = self.root
        
        while (True) :
            if temp.value == new.value:
                return False
            
            if temp.value > new.value:
                if temp.left is None:
                    temp.left = new
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new
                    return True
                temp = temp.right

    def containsWhile(self, value):
        if self.root is None:
            return False
        
        temp = self.root
        
        while temp:
            if temp.value == value:
                return True
            
            if temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        
        
        #no es lo mismo si lo dejas adentro siempre tienes que ponerlo afuera!!!
        
        return False
    
def contains(root, value):
    if root is None:
        return False
    
    #root es tu temp
    
    if root.value == value:
        return True
    elif root.value > value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)
    
def getHeight(node):
    if node is None:
        return 0
    
    hLeft = getHeight(node.left)
    hRight = getHeight(node.right)
    
    return max(hLeft,hRight) + 1

#balance se considera si la diference entre alutra izq y alt der son 0 o 1, no mas de 1
def isBalanced(node):
    if node is None:
        return False
    
    h1 = getHeight(node.left)
    h2 = getHeight(node.right)
    
    if abs(h1-h2) <=1:
        return True
    else:
        return False
        
            
        
        
            
myTree = BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.insert(4)
myTree.insert(8)
myTree.insert(9)
print(myTree.root.value)
print(myTree.root.left.value)          
print(myTree.root.right.value)   
print(isBalanced(myTree.root))


    
    
    