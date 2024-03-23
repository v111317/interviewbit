#https://www.interviewbit.com/problems/remove-consecutive-characters/

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        n = B
        str1 = A
        buffer = []
        result = []
    
        buffer.append(str1[0])
        count = 1
        for i in range(1, len(str1)):
            
            if str1[i]==str1[i-1]:
                buffer.append(str1[i])
                count += 1
            else:
                if count!=n:
                    result += buffer
                
                buffer = [str1[i]]
                count = 1
                
        if len(buffer)!=n:
            result += buffer
        return "".join(result)
    
sol1 = Solution()
# print(sol1.solve("aabcd", 2))    
# print(sol1.solve("aabbccd", 2))  
# print(sol1.solve("aaabbccd", 2))  
str1 = "lfoajnippckfilmebjffjdacopakmhfbfagnoekojnaieolalehfdonhlpomflkcjhbkmknnciaehfbgliklmjhfmpmjpgcghcnkjfgcmbhcinljcncbmmhedboffhnnogmhfehdcfhlidohlffppmjccafimiigngfbmcdphcdgghcalijlnhmhpkoaogodmpoofpfdbdnakhkdkmekioemmbnaifbjddcgeheoehfefcjjnjmhdpfapgeifgdelgnghkhcjlfbajbldlnnpciofpplkididngalglikambfgpbojioamkaflmecccbpffchepgahbfhnfmnhlkhkfllniacehdmpfdklokdphjgmcgpfaajlkieojhffipeegjodcmfcbnmgfpenhfembheleahdgfiplbobifeimamepfeclbokjpklanpaanaiidmnaiploieogbpdfnokpjflknhjfcbgcfojiokjfohmkjdbmcceanjanhbcdocglbkgjaefejaejimpkidejkihjiedhghmoilofcijfoabnkcbjjbbahlpnigppkoniccjlclhgnpfaobmkfclijllafie"
print(sol1.solve(str1, 1))    
    
            
            
            
        