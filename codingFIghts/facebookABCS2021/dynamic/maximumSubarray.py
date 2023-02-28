#no pienses que por ser dynamic ahuevo tienes que hacer recursion, 
#simplemente es ir acumulando para no regresarte hacia atras en un proceso
class Solution(object):
    def maxSubArray(self, nums):
    
        maxTemp = 0
        maxTotal = -10000



        for i in range(0,len(nums)):
            #va acumulando todo 
            maxTemp += nums[i]
            
            #si un numero es mayor que toda la la suma acumulada se pone como el max temp
            if nums[i] > maxTemp:
                maxTemp = nums[i]
            
            #si ese nuevo maxTemp es mayor al maximo encontrado anteriormente, se actualiza
            if maxTemp > maxTotal:
                maxTotal = maxTemp

        return maxTotal

            

        
        
        