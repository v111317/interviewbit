class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    #time limit exceeded
    def solve(self, A, B):
        sizeA = len(A)
        #print(sizeA)
        windowLen = B
        
        startMax = 0
        endMax = 0
        maxSum = float('-inf')
        for i in range(sizeA-windowLen, sizeA+windowLen):
            if i%sizeA==0:
                break
            sumNums = 0
            k = i
            for j in range(0, windowLen):
                sumNums += A[k%sizeA]
                j += 1
                k += 1
            
            if sumNums > maxSum:
                
                startMax = i
                endMax = i + windowLen
                #print(sumNums, maxSum, startMax, endMax)
                maxSum = sumNums
                
        return maxSum

    def solve2(self, A, B):
        sizeA = len(A)
        #print(sizeA)
        windowLen = B
        
        maxSum = float('-inf')
        sumNums = 0
        
        k = sizeA-windowLen
        for i in range(windowLen):
            sumNums += A[k%sizeA]
            k += 1
        maxSum = max(maxSum, sumNums)
        #print(maxSum)
        
        for i in range(sizeA-windowLen+1, sizeA+1):
            #print(" => ", (i-1)%sizeA, A[i%sizeA])
            sumNums -= A[(i-1)%sizeA]
            #print(" => ", (i+windowLen-1)%sizeA, A[(i+windowLen-1)%sizeA])
            sumNums += A[(i+windowLen-1)%sizeA]
            #print(sumNums, maxSum)
            maxSum = max(maxSum, sumNums)
                
        return maxSum
    
sol1 = Solution()
#print(sol1.solve2([5, -2, 3 , 1, 2], 3))
print(sol1.solve2([1, 2], 1))
list1  =[ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
print(sol1.solve2(list1, 48))
list2 = [ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ]
print(sol1.solve2(list2, 81))
#6253