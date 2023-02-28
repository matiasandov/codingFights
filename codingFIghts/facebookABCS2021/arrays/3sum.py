#FUNCIONA PERO LEETCODE ESPERA MENOR COMPLEJIDAD
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #computar todas los posibles triplets
        #guardar combinaciones unicas en el set
        res = []
        
        if len(nums) < 3:
            return []
        
        else:
            
            
            for i in range(0, len(nums)):
                for j in range(0, len(nums)):
                    for k in range(0, len(nums)):
                        
                        if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k] == 0):
                            
                            temp = [nums[i],nums[j], nums[k]]
                            
                            #si lo ordenas siempre, podras encontrar repetidos mas facil
                            temp.sort()
                            #no puedes hacer un set de listas en python por lo que se solucionaria agregando todo en una lista y al final remover los duplicados, en lugar de ocupar un set
                            res.append(temp)
            
            #
            resF = []
            #AGREGAR SOLO LOS VALORES UNICOS, O SEA SI SE REPITEN, AGREGA SOLO UNA VEZ EL REPETIDO
            for k in res:
                if k not in resF:
                    resF.append(k)
        return resF
    