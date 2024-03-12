#https://www.interviewbit.com/problems/palindrome-string/

# Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, 
# case, and all special characters; i.e. consider only alphanumeric characters.

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        strLen = len(A)
        i = 0
        end = strLen - i - 1
        isStartValid = False
        isEndValid = False
        while i <= end:
            
            if (A[i] >= '0' and A[i] <= '9') or (A[i] >= 'A' and A[i] <= 'Z') or (A[i] >= 'a' and A[i] <= 'z'):
                isStartValid = True
            else:
                isStartValid = False
                i += 1
            
            if (A[end] >= '0' and A[end] <= '9') or (A[end] >= 'A' and A[end] <= 'Z') or (A[end] >= 'a' and A[end] <= 'z'):
                isEndValid = True
            else:
                isEndValid = False
                end -= 1
            
            if isStartValid and isEndValid:
                #print(i, end, A[i], A[end])
                if A[i].lower()!=A[end].lower():
                    return 0
                else:
                    i += 1
                    end -= 1
                    isStartValid = False
                    isEndValid = False
                
        return 1
    
sol1 = Solution()
print(sol1.isPalindrome("A man, a plan, a canal: Panama"))
print(sol1.isPalindrome("race a car"))
