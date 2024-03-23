#https://www.interviewbit.com/problems/counting-triangles/

class Solution:
	# @param A : list of integers
	# @return an integer
    #time limit exceeded
    def nTriang(self, A):
        n = len(A)
        if n <= 2:
            return 0

        result = 0
        for num in range(7, pow(2, n)):
            i = 0
            sides = []
            while num!=0:
                if num & 1 == 1:
                    sides.append(A[i])
                    if len(sides)>3:
                        sides = []
                        break
                num = num >> 1
                i += 1
            if len(sides)==3 and (sides[0]<sides[1]+sides[2]) and (sides[1]<sides[2]+sides[0]) and (sides[2]<sides[0]+sides[1]):
                result += 1
        
        return result % (pow(10,9)+7)
    
    def nTriang2(self, A):
        a = 1
        nums = A
        nums.sort()
        
sol1  = Solution()
print(sol1.nTriang([1, 1, 1, 2, 2]))