class BstNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def insert_into_binary_tree(root: BstNode, value):
   
    #si ya llegaste a la leaf, creas el nodo
    if(root is None):
        #regresas nodo creado
        root = BstNode(value)
    #si se encuentra el value, no lo insertas, regresas el que ya esta
    
    elif(value >= root.value):
        #vas a ir guardando en izq o der lo que se va poniendo
        #cont = cont + 1
        #si el valor deseado a ingresar es mas grande que root, te vas hacia la derecha
        root.right = insert_into_binary_tree( root.right, value)
    else:
        #cont = cont + 1
        #vas a ir guardando en izq o der lo que se va poniendo
        root.left =  insert_into_binary_tree(root.left, value)
    
    return root
    