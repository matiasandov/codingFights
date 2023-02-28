#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#time complexity is O^2 (2 nested loops
# space complexity: O(1) beacuse you only need to store a constant value (2 integers always)
#not depending of an n length
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #recorres cada elemento
        for i in range(len(nums)):
            #recorres los siguientes elementos a i
            for j in range(i + 1, len(nums)):
                #si encuentras en j el numero que  es el complemento (si le restas i al target te debe dar el complemento)
                if nums[j] == target - nums[i]:
                    return [i, j]