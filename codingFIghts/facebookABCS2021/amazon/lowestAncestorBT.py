class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]

        """

        checas rooti.left o/y rooti.right esta en nodes, si si regresas rooti a su parent 
        si no esta regresas null
        

        """
        nodes = set(nodes)

        def dfs(node):
            if node is None:
                return None
            
            #condicion para BUSCAR
            if node in nodes:
                return node
            
            l = dfs(node.left)
            r = dfs(node.right)

            #si contiene ambos se regresa root
            if l and r:
                return node 
            #si contiene alguno de los dos se mueve hacia abajo donde no sea None
            else:
                return l or r

        return dfs(root)

        