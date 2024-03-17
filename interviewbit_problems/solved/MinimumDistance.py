class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        xArr = []
        oArr = []
        lastSeenXIdx = -1
        lastSeenOIdx = -1
        
        for i in range(len(A)):
            if A[i]=='x':
                lastSeenXIdx = i
            elif A[i]=='o':
                lastSeenOIdx = i
            
            if lastSeenXIdx > -1:
                xArr.append(abs(i-lastSeenXIdx))
            else:
                xArr.append(-1)
                
            if lastSeenOIdx > -1:
                oArr.append(abs(i-lastSeenOIdx))
            else:
                oArr.append(-1)
        
        if lastSeenOIdx==-1 or lastSeenXIdx==-1:
            return -1
        
        lastSeenXIdx = -1
        lastSeenOIdx = -1
        for i in range(len(A)-1,-1,-1):
            if A[i]=='x':
                lastSeenXIdx = i
            elif A[i]=='o':
                lastSeenOIdx = i
            
            if lastSeenXIdx > -1:
                if xArr[i]==-1:
                    xArr[i] = abs(i-lastSeenXIdx)
                else:    
                    xArr[i] = min(abs(i-lastSeenXIdx), xArr[i])
                
            if lastSeenOIdx > -1:
                if oArr[i]==-1:
                    oArr[i] = abs(i-lastSeenOIdx)
                else:
                    oArr[i] = min(abs(i-lastSeenOIdx), oArr[i])
        minDiff = float('inf')
        for i in range(len(A)):
            if A[i]=='x' or A[i]=='o':
                diff = abs(oArr[i]-xArr[i])
                if diff < minDiff:
                    minDiff = diff     
        
        return minDiff

sol1 = Solution()
print(sol1.solve("x...o.x...o"))
print(sol1.solve("xxx...xxx"))
