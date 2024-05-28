# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
borrar elementos que te dicen
y dejas arboles individuales de ser necesario
1. borras checan si el valor esta dentro de to delete
        to delete lo puedes hacer un set para busqueda instantanea        

2. los que quedan, el de hasta arriba sera ahora una leaf y guardaras su root en resultado
    los left y right ahora seran roots a menos que no haya
    se debe buscar ahora en left and right si hay elementos por encontrar
"""
class Solution:


    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        forest = []
        toDel = set(to_delete)
        
        """
        #when you do it inside you dont need to pass lists
        we need a way to for everytime there is root, start a new list
        """
        def dfs(root, rootFlag):
            if root is None :
                return None

            if root.val in toDel:
                #new roots
                dfs(root.left, True)
                dfs(root.right, True)
                #root = None
                return None

            else:
                if rootFlag:
                    forest.append(root)
                #connect right and left to the root to append it to the list
                root.left = dfs(root.left, False)
                root.right = dfs(root.right, False)
                #si no regresas esto no se conectan root.left and root.right
                #cada vez que haces return se corta la lista 
                return root

        
        dfs(root, True)
        return forest
                
                    