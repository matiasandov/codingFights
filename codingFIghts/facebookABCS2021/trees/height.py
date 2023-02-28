class BinarySearchTreeNode:
    #asi inicializas un arbol
    #se iniciliza con node_Data que sera data 
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None

def insert_node_into_binary_search_tree(node, node_data):
    #si el nodo es null -> o sea el actual
    if node == None:
        #se inicia un nodo con el data que le pasaron
        node = BinarySearchTreeNode(node_data)
    else:
        #si no es nulo (ya tiene data ela ctual)
        if (node_data <= node.data):
            #a la izquierda se insertara su nodo izq y se recursiona
            node.left = insert_node_into_binary_search_tree(node.left, node_data)
        else:
            # a la derecha se insertara su nodo derecho recursionando
            node.right = insert_node_into_binary_search_tree(node.right, node_data)

    return node

#imprime en transversal
def print_binary_search_tree_inorder_traversal(node, sep, fptr):
    if node == None:
        return

    print_binary_search_tree_inorder_traversal(node.left, sep, fptr)

    if node.left:
        fptr.write(sep)
    fptr.write(str(node.data))

    if node.right:
        fptr.write(sep)

    print_binary_search_tree_inorder_traversal(node.right, sep, fptr)

#le pasas de parametro todo el arbol ya hecho
#def bst_height(bst):
def bst_height(root: BinarySearchTreeNode ):
    #root realemnte es el nodo actual, no necesariamente el root real
    if root is None:
        return 0
    #se sacara altura de todo el subtree izq 
    heightLeft = bst_height(root.left)
    heightRight = bst_height(root.right)
    #por cada recursion hacia cualquier lado ira regresan +1 y la max height actual hasta determinado nodo
    #y al final si devovlera la formula real que es el la altura maxima entre los dos subtrees mas 1
    return 1 + max(heightLeft, heightRight)


#para que funcionara tuve que restarle -1 a la height total 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_bst_count = int(input().strip())

    input_bst = None

    for _ in range(input_bst_count):
        input_bst_item = int(input().strip())
        input_bst = insert_node_into_binary_search_tree(input_bst, input_bst_item)

    height = bst_height(input_bst)
    #solo asi funciono
    height = height - 1
    fptr.write(str(height) + '\n')

    fptr.close()