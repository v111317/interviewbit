class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minNum = float('inf')
        maxNum = float('-inf')
        
        for num in A:
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        
        return maxNum+minNum
    #solve for min no. of comparisons
    
sol1 = Solution()
print(sol1.solve([-2, 1, -4, 5, 3]))