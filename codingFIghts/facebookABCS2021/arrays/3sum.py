#FUNCIONA PERO LEETCODE ESPERA MENOR COMPLEJIDAD
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]


        la logica esta en que existen positivos, negativos y zeros
        si te das cuenta, las unicas combinaciones posibles deberan ser
        - 1 positivo 2 negativos
        - 1 negativo, 2 positivos
        - 1 neg, 1 pos , y 0 -> donde ambos digitos son iguales
        - 3 zeros

        Entonces para esto puedes buscar sus complementos de todos
        """
        res = set()

        n = []
        p = []
        z = []

        for i in nums:
            if i > 0:
                p.append(i)
            elif i == 0:
                z.append(i)
            else:
                n.append(i)

        #
        if len(z) >= 3:
            res.add((0,0,0))
        
        #crear sets para busqueda O(1)
        setP = set(p)
        setN = set(n)

        #buscar numeros digitos iguales que sumen 0
        if len(z) > 0:
            for i in p:
                if i*-1 in setN:
                    res.add((i, i*-1, 0))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                complement = -1*( p[i] + p[j])
                if complement in setN:
                    temp = [p[i], p[j], complement]
                    temp.sort()
                    res.add(tuple(temp))
        
        for i in  range(len(n)):
            #esta es la parte mas importante sino no funciona
            for j in range(i+1, len(n)):
                complement = (n[i] + n[j])*-1
                if complement in setP:
                    temp = [n[i],n[j], complement]
                    temp.sort()
                    res.add(tuple(temp))
        #nota que en las instrucciones dice que puedes regresar un set aunque los outputs aparezca un array de arrays
        return res




        
    
    
    def threeSum_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #computar todas los posibles triplets
        #guardar combinaciones unicas en el set
        res = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i!= k and i != j and j != k and nums[i] + nums[j] + nums[k] == 0 :
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        res.add(tuple(temp))
        new = []
        for i in res:
            new.append(list(i))

        return new
                        
    