class findK(object):
    #constructor
    def __init__(self, array):
        self.nums = array
        self.k = 0
    def find(self):
        for  i in range(len(self.nums)):
            if self.nums[i] > self.k:
                self.k = self.nums[i]
    
        
        
        