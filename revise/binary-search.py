class Solution:
    
    #iterative
    def solveByBinarySearch(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end+start)//2
            if target > nums[mid]:
                start = mid+1
            elif target < nums[mid]:
                end = mid-1
            else:
                return mid
        return -1
    
    #recursive
    def solveByBinarySearch2(self, nums, target, start, end):
        mid = (start+end)//2
        if nums[mid]==target:
            return mid
        elif start > end:
            return -1
        
        if target > nums[mid]:
            return self.solveByBinarySearch2(nums, target, mid+1, end)
        else:
            return self.solveByBinarySearch2(nums, target, start, mid-1)
        
    

sol1 = Solution()
# print(sol1.solveByBinarySearch([1,5,6,9,10,20,31,43], 5))
# print(sol1.solveByBinarySearch([1,5,6,9,10,20,31,43], 1))
# print(sol1.solveByBinarySearch([1,5,6,9,10,20,31,43], 43))
# print(sol1.solveByBinarySearch([1,5,6,9,10,20,31,43], 40))
                
print(sol1.solveByBinarySearch2([1,5,6,9,10,20,31,43], 5, 0, 7))
print(sol1.solveByBinarySearch2([1,5,6,9,10,20,31,43], 1, 0, 7))
print(sol1.solveByBinarySearch2([1,5,6,9,10,20,31,43], 43, 0, 7))
print(sol1.solveByBinarySearch2([1,5,6,9,10,20,31,43], 40, 0, 7))