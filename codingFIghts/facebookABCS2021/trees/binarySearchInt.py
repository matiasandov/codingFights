class BinarySearchTreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None

def bst_contains(root: BinarySearchTreeNode, number):
    if root is None:
        return 0

    if(root.data == number):
        return 1
    elif(root.data < number):
        #si int es mas grande que el data actual, buscas en derecha
        #-----------return es importantitismo------------
        return bst_contains(root.right, number)

    elif(root.data > number):
        #si int es mas pequeno que el data actual, buscas en derecha
         #-----------return es importantitismo------------
        return bst_contains(root.left, number)
