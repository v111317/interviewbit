#https://www.interviewbit.com/problems/number-of-1-bits/

#Write a function that takes an integer and returns the number of 1 bits it has.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        binNum = bin(A)
        binNum = binNum[2:]
        
        result = 0
        for ch in binNum:
            if ch == "1":
                result += 1
                
        return result

sol1 = Solution()
print(sol1.numSetBits(11))