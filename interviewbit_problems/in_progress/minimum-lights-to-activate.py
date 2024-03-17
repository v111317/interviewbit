class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        bulbs = A
        power = B
        
        i = 0
        while i < len(A):
            