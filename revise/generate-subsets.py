class Solution:
    
    def genSubset(self, nums):
        n = len(nums)
        
        result = []
        for i in range(1<<n):
            for j in range(0, 1):
                a = 1
    