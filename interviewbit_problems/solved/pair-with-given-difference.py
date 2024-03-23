#https://www.interviewbit.com/problems/pair-with-given-difference/

# Given an one-dimensional unsorted array A containing N integers.
# You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
# Return 1 if any such pair exists else return 0.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        if len(A)==1:
            return 0
        
        nums = A
        diff = abs(B)
        
        nums.sort()
        
        for i in range(len(nums)-1):
            num = nums[i]
            
            start = i+1
            end = len(nums)-1
            
            if nums[start]-num==diff or nums[end]-num==diff:
                return 1
            
            while start <= end:
                mid = (start+end)//2
                
                if nums[mid]-num>diff:
                    end = mid - 1
                elif nums[mid]-num < diff:
                    start = mid + 1
                else:
                    return 1
        return 0

    def solve2(self, A, B):
        
        if len(A)==1:
            return 0
        
        nums = A
        diff = B
        
        numMap = {}
        numDiff1 = 0
        numDiff2 = 0
        
        for num in nums:
            numDiff1 = num+diff
            if diff < 0:
                numDiff2 = num-diff
            if num in numMap:
                return 1
            else:
                numMap[numDiff1] = 1
                if diff < 0:
                    numMap[numDiff2] = 1
        return 0
    
sol1 = Solution()
print(sol1.solve2([5, 10, 3, 2, 50, 80], 78))
print(sol1.solve2([-10, 20], 20))

list1 = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]
print(sol1.solve2(list1, -42))            
