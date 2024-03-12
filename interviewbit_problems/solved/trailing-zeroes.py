#https://www.interviewbit.com/problems/trailing-zeroes/

#Given an integer A, count and return the number of trailing zeroes

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        binNum = bin(A)
        binNum = binNum[2:]
        strLen = len(binNum)
        
        count = 0
        for i in range(strLen-1, -1, -1):
            if binNum[i] == "0":
                count += 1
            else:
                return count

sol1 = Solution()
print(sol1.solve(8))