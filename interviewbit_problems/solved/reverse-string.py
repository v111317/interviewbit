#https://www.interviewbit.com/problems/reverse-string/

# Given a string S, reverse the string using stack.

# Example :

# Input : "abc"
# Return "cba"

class Solution:
	# @param A : string
	# @return a strings
    def reverseString(self, A):
        if len(A)<=1:
            return A
        
        stk1 = []
        
        for letter in A:
            stk1.append(letter)
    
        revStr = ""
        while len(stk1)!=0:
            revStr += stk1.pop()
            
        return revStr

sol1 = Solution()
print(sol1.reverseString("abc"))
