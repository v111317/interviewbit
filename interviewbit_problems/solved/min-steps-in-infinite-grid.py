#https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps = 0
        i = 0
        while i < len(A)-1:
            steps += max(abs(A[i+1]-A[i]), abs(B[i+1]-B[i]))
            i += 1
        return steps

sol1 = Solution()
print(sol1.coverPoints([0, 1, 1], [0, 1, 2]))