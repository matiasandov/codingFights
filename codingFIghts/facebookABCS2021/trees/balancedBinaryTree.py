#It is balanced if the difference in height between the left and right tree is between zero and one
#o sea puede ser 0 o como max 1, mas de 1 ya se considera no balanced

"""
yo pienso que debo tomar la height de todo el left y la height de todo el right y al final comparar

en el subtre left iugal habra right y left e igual en subtree right, la height de un subtre debe ser la 

max entre heightleft y height right
"""

def getHeight(node):
    #una vez que llegas aca re
    if node is None:
        return 0
    
    hLeft = getHeight(node.left)
    hRight = getHeight(node.right)
    
    #por cada nivel se regresa 1
    return max(hLeft, hRight) + 1
        
 
def balancedTree(root):
    if root is None:
        return False
    
    h1 = getHeight(root.left)
    h2 = getHeight(root.right)
    
    if abs(h1-h2) <= 1:
        return True
    else: 
        return False
        
    