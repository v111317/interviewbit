#https://www.interviewbit.com/problems/amazing-subarrays/

# You are given a string A, and you have to find all the amazing substrings of A.
# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
# Note: Take the mod of the answer with 10003.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelCount = 0
        consonantCount = 0
        strLen = len(A)
        
        result = 0 
        for i, ch in enumerate(A):
            if ch.lower() in vowels:
                result += strLen - i
        
        return result % 10003
            
sol1 = Solution()
print(sol1.solve("ABEC"))
                 
                