class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #constraints
        #can the element i in the sequence be the same as the target? no
        
        #para lograr esto necesitas usar una hash table
        # for i in len(nums):
        #     if nums[i] > target:
        #         continue
        #     else:
        #         if target - nums[i] in nums:
        #             return [i, other index]

        #inicializar hash table vacia

        hash = {}

        #es bueno guardar len para no estarlo haciendo cada vez
        n = len(nums)

        for i in range(n):
            #key, value
            #valor, posicion -> asi puedo buscar por key en 0(1)
            hash[nums[i]] = i
        
        #recorres diccionario y array a la par
        for i in range(n):
            y = target - nums[i] 
            if y in hash and hash[y] != i:
                return [i, hash[y]]
        
        #tienes que preguntar!!
        #sino regresar vacio
        return []

            
