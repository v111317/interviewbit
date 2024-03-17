class Solution:
    # @param A : list of integers
    # @return an integer
    #time limit exceeded
    def solve(self, A):
        splElements = 0
        sumEven = 0
        sumOdd = 0
        j = 0 
        for i in range(len(A)):
            j = 0
            sumEven = 0
            sumOdd = 0
            while j < len(A):
                if j < i:
                    if j%2==0:
                        sumEven += A[j]
                    else:
                        sumOdd += A[j]
                elif j > i:
                    if j%2==0:
                        sumOdd += A[j]
                    else:
                        sumEven += A[j]
                j += 1
            #print(i, A[i], sumEven, sumOdd)
            if sumEven==sumOdd:
                splElements += 1
        return splElements

sol1 = Solution()
print(sol1.solve([2, 1, 6, 4]))
print(sol1.solve([5, 5, 2, 5, 8]))