#https://www.interviewbit.com/problems/intersection-of-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linked_list import Node
from linked_list import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        numMap = {}
        i = 0
        
        headA = A
        headB = B
        
        ptr = headA
        while ptr!=None:
            numMap[ptr.val] = i
            i += 1
            ptr = ptr.next
        
        # print(numMap)
        ptr = headB
        i = -1
        minIdx = float('inf')
        matchedIdx = -1
        while ptr!=None:
            i += 1
            if ptr.val in numMap:
                
                
                if matchedIdx==-1:
                    matchedIdx = numMap[ptr.val]
                else:
                    if numMap[ptr.val] < matchedIdx:
                        matchedIdx = numMap[ptr.val]
                        minIdx = float('inf')
                        
                minIdx = min(minIdx, i)
                #print(" => ", ptr.val, minIdx, matchedIdx)
            else:
                minIdx = float('inf')
                
            #print(ptr.val, i, minIdx)
            ptr = ptr.next
            
        if minIdx!=float('inf'):
            count = 0
            ptr = headB
            while ptr!=None:
                if count==minIdx:
                    return ptr.val
                ptr = ptr.next
                count += 1
        else:
            return None
        
    def getIntersectionNode2(self, A, B):
        headA = A
        headB = B
        
        ptrMap = {}
        
        ptr = headA
        while ptr!=None:
            ptrMap[ptr] = ptr.val
            ptr = ptr.next
            
        ptr = headB
        while ptr!=None:
            if ptr in ptrMap:
                return ptr
            ptr = ptr.next
        
        return None


ll1 = LinkedList()
ll1Head = None
list1 = [76, 21, 20, 50, 46, 91, 76, 74, 23, 18, 73, 14]#[1,2,3,4,5, 2, 3, 4, 5,5,6,7]
for i in list1:#[22,6,67,5,1, 23, 62, 60]:
    ll1.insertAtEnd(i)

ll2 = LinkedList()    
list2 = [43, 63, 17, 84, 15, 71, 60, 73, 76,  74, 23, 18, 73, 14]#[10,9,8,5,6,7]
for i in list2:#[11, 62, 23, 62, 60]:
    ll2.insertAtEnd(i)

ll1.printList()
ll2.printList()

sol1 = Solution()
print(sol1.getIntersectionNode2(ll1.head, ll2.head))

# 7 76 21 20 50 46 91 76
# 9 43 63 17 84 15 71 60 73 76
# 5 74 23 18 73 14
            
                
            