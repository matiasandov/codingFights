#el el min debe estar en incio y max debe estar en final, habi duplicados
#hazlo en los minimos swaps posible
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        #Encontrar el min en mas izq
        minVal = min(nums)
        posMin = 0

        while posMin <= len(nums):
            if nums[posMin] == minVal :
                break
            else:
                posMin += 1
        
        #Encontrar max mas derecho
        maxVal= max(nums)
        posMax = len(nums)-1

        while posMax >= 0:
            if nums[posMax] == maxVal:
                break
            else: 
                posMax -= 1
        #si ya esta en min ya esta en inicio y max esta en final
        if posMax == len(nums)-1 and posMin == 0:
            return 0

        #creo que saltos  para cada numero -1 al final sera la respuesta
        stepsRight = (len(nums)-1 )- posMax
        
        if posMax < posMin:
            #asi se interceptan
            steps = posMin + stepsRight - 1
        else:
            #asi no se interceptan
            steps = posMin + stepsRight 

        return steps
