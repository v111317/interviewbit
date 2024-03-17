class Solution:
	# @param A : list of integers
	# @return an integer
    def solve(self, A):
        A.sort()
        i = 0
        print(A)
        while i < len(A)-1:
            if A[i]!=A[i+1]:
                if len(A)-1-i==A[i]:
                    return 1
            i += 1
        if i == len(A)-1:
            if abs(A[i])==0:
                return 1
        return -1
    
sol1 = Solution()
# print(sol1.solve([3, 2, 1, 3]))   
# print(sol1.solve([1, 1, 3, 3]))  
# print(sol1.solve([ -4, -2, 0, -1, -6 ]))     
# print(sol1.solve([ -1, -2, 0, 0, 0, -3 ]))  
print(sol1.solve([ -6, -1, 4 ]))
   