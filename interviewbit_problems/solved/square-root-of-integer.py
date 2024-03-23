#https://www.interviewbit.com/problems/square-root-of-integer/

# Given an integer A.
# Compute and return the square root of A.
# If A is not a perfect square, return floor(sqrt(A)).
# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

# NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.
import math

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        previous = 0
        new = A
        while math.floor(previous)-math.floor(new)!=0:
            mid = (previous+new)/2
            
            if pow(mid, 2) > A:
                new = mid
            else:
                previous = mid
        return math.floor(previous)
            
sol1 = Solution()
print(sol1.sqrt(11))
print(sol1.sqrt(9))
print(sol1.sqrt(0))
        