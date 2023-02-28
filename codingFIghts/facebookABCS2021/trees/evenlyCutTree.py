# Inputs
# #t_nodes: numero de nodes
# #t_edges: numero de edges
#  #t_from: cuantos nodos tienen t_edges
#  #t_to: nodos finales conectados a cada edge
# ejemplos:
# 10
# 9 
# 2 3 4 5 6 7 8 9 10
# 1 1 3 2 1 2 6 8 8

 #Output: Print the number of removed edges.

#tenemos que calcular recursivamente 
# 1.altura de los dos subtrees 
#2. encontrar el nodo donde se hara el corte

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#regresa un tree node
def cut_tree(root: TreeNode) -> TreeNode:
    #cuenta nodos
    total_nodes = count_nodes(root)
    return find_cut(root, total_nodes)

def count_nodes(node: TreeNode) -> int:
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def find_cut(node: TreeNode, total_nodes: int) -> TreeNode:
    if not node:
        return None
    
#se calculan el numero de nodos de cada lado para el input dado
    left_nodes = count_nodes(node.left)
    right_nodes = count_nodes(node.right)
    #si la altura de cada lado es diferente se regresa nodo para seguir iterando
    if abs(left_nodes - right_nodes) > 1:
        return node
    #si ya es el cut node se regresa este mismo ya que las condiciones de abajo
    #no se cumpliran

    #si el numero de nodos es mayor que la mitad de todos los nodos del arbol
    #si itera para la izq
    if left_nodes > total_nodes // 2:
        return find_cut(node.left, left_nodes)
    else:
        #mismo caso pero con derecha
        return find_cut(node.right, right_nodes)


