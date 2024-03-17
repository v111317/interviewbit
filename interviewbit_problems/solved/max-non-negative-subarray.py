class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sum = 0
        maxSum = 0
        startMax = 0
        endMax = 0
        start = 0
        segLen = 0 
        sumMap = {}
        
        for i, num in enumerate(A):
            if num >=0:
                sum += num
            else:
                if sum >= maxSum:
                    
                    startMax = start
                    endMax = i - 1
                    segLen = endMax-startMax+1
                    # print(sum, maxSum)
                    # for i in range(startMax, endMax+1): 
                    #     print(A[i])
                    # print("\n")
                    if sum==maxSum:
                        if segLen not in sumMap:
                            sumMap[segLen] = []
                            
                        sumMap[segLen].append([startMax, endMax])
                    else:
                        sumMap = {}
                        sumMap[segLen] = [[startMax, endMax]]
                        maxSum = sum 
                sum = 0
                    
                start = i + 1    
        if sum >= maxSum:
            startMax = start
            endMax = i
            segLen = endMax-startMax+1
            if sum==maxSum:
                if segLen not in sumMap:
                    sumMap[segLen] = []
                    
                sumMap[segLen].append([startMax, endMax])
            else:
                sumMap = {}
                sumMap[segLen] = [[startMax, endMax]]
                maxSum = sum
        
        maxLen = max(list(sumMap.keys()))
        startMax, endMax = sumMap[maxLen][0]
        
        result = []        
        for i in range(startMax, endMax+1):
            result.append(A[i])
        return result

sol1  = Solution()
# print(sol1.maxset([1, 2, 5, -7, 2, 3]))
# print(sol1.maxset([10, -1, 2, 3, -4, 100]))
# print(sol1.maxset([-1, -1, -1, -1, -1]))
# print(sol1.maxset([0, 0, -1, 0, 0]))
# print(sol1.maxset([ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]))
list1 = [ 24831, 53057, 19790, -10679, 77006, -36098, 75319, -45223, -56760, -86126, -29506, 76770, 29094, 87844, 40534, -15394, 18738, 59590, -45159, -64947, 7217, -55539, 42385, -94885, 82420, -31968, -99915, 63534, -96011, 24152, 77295 ]
print(sol1.maxset(list1))
