class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#regresa un bool true or false
def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    #si la resta de las alturas no es 0, no esta balanceado
    if abs(left_height - right_height) > 1:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)

def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    #regresa un integer que represents la height del bst rooted en el nodo dado.
    return max(left_height, right_height) + 1
