class BinarySearchTreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None

def preorder_traversal(root: BinarySearchTreeNode):
    if root is None:
        return
    #------aqui no necesitas hacer return porque imprimes
    #imprimes primero el actual
    print(root.data)
    #despues te vas izq 
    preorder_traversal(root.left)
    #por ultimo te vas a derecha
    preorder_traversal(root.right)
    