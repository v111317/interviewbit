#https://www.interviewbit.com/problems/min-xor-value/

# Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. 
# Report the minimum XOR value.

class Solution:
	# @param A : list of integers
	# @return an integer
 
    #time limit exceeded
    def findMinXor(self, A):
        A.sort()
        minXor = float('+inf')
        
        for i in range(len(A)-1):
            
            xor = A[i] ^ A[i+1]
            minXor = min(minXor, xor)
        
        return minXor

sol1 = Solution()
print(sol1.findMinXor([0, 2, 5, 7]))
print(sol1.findMinXor([0, 4, 7, 9]))

        