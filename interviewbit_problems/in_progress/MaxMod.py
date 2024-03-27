class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mod = 0
        maxMod = -1
        i = 1
        j = 0
        A.sort()
        while i < len(A):
            j = i - 1
            maxMod = max(A[i]%A[len(A)-1], maxMod)
            while j >= 0:
                if A[j]!=0:
                    mod = A[i] % A[j]
                    maxMod = max(maxMod, mod)
                    j -= 1
            i += 1
        return maxMod
    def solve2(self, A):
        if len(A)==1:
            return A[0]
        
        lenA = len(A)
        A.sort()
        i = lenA-1
        while i >= 0:
            if A[i]!=A[i-1]:
                return A[i-1]
            i -= 1
        return 0
                
        

sol1 = Solution()
print(sol1.solve2([1, 2, 44, 3]))
print(sol1.solve2([2, 6, 4]))
print(sol1.solve2([2, 2, 2]))
print(sol1.solve2([1, 2, 3, 3]))