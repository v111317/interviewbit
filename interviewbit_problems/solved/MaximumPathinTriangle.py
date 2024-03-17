class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        mem = {}
        
        return self.findSum(A, mem, 0, 0)
        
    def findSum(self, A, mem, i, j):
        #print(i, j, A[i][j], mem)
        
        key = str(i) + "_" + str(j)
        if key in mem:
            return mem[key]
        
        if i == len(A)-1:
            return A[i][j]
        
        keyDown = str(i+1) + "_" + str(j)
        if keyDown in mem:
            sumLeft = mem[keyDown]
        else:
            sumLeft = self.findSum(A, mem, i+1, j)
            mem[keyDown] = sumLeft
        
        keyAcross = str(i+1) + "_" + str(j+1)
        if keyAcross in mem:
            sumAcross = mem[keyAcross]
        else:
            sumAcross = self.findSum(A, mem, i+1, j+1)
            mem[keyAcross] = sumAcross
    
        mem[key] = A[i][j] + max(sumLeft, sumAcross)
        return mem[key]

sol1 = Solution()
A = [
        [3, 0, 0, 0],
        [7, 4, 0, 0],
        [2, 4, 6, 0],
        [8, 5, 9, 3]
]
B = [
        [8, 0, 0, 0],
        [4, 4, 0, 0],
        [2, 2, 6, 0],
        [1, 1, 1, 1]
     ]
print(sol1.solve(B))
print(sol1.solve(A))