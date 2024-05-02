def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indexPointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                print("------------")
                print(" pointer:  ", indexPointer)
                nums[indexPointer] = nums[i]
                print("nums[indexPointer]: ",nums[indexPointer])
                indexPointer += 1
                print("increase pointer indexPointer += 1:  ", indexPointer)
        
        print("array ", nums)
        print("final ", indexPointer)
        return indexPointer

removeElement([0,1,2,2,3,0,4,2], 2)