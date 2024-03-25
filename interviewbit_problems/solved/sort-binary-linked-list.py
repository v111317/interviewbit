#https://www.interviewbit.com/problems/sort-binary-linked-list/

# Given a Linked List A consisting of N nodes.
# The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.
# You need to sort the linked list and return the new linked list.
# NOTE:
# Try to do it in constant space.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

from linked_list import LinkedList

class Solution:
    
    def insertAtBegin(self, head, node):
        if head==None:
            head = node
            return head
        
        ptr = head
        node.next = ptr
        
        return node
    
    def insertAtEnd(self, head, node):
        if head==None:
            head = node
            return head
        
        ptr = head
        while ptr.next!=None:
            ptr = ptr.next
        
        ptr.next = node
        return head
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    #time limit exceeded
    def solve(self, A):
        headA = A
        
        if headA==None:
            return A
        
        newHead = None
        
        ptr = headA
        
        while ptr!=None:
            nextPtr = ptr.next
            ptr.next = None
            if ptr.val == 0:
                newHead = self.insertAtBegin(newHead, ptr)
            else:
                newHead = self.insertAtEnd(newHead, ptr)
            ptr = nextPtr
            #ptr = ptr.next

        return newHead
    
    def solve2(self, A):
        
        headA = A
        if headA==None:
            return headA
        
        zerosCount = 0
        onesCount = 0
        
        ptr = headA
        
        while ptr!=None:
            if ptr.val==0:
                zerosCount += 1
            else:
                onesCount += 1
            ptr = ptr.next
        
        ptr = headA
        count = 1
        while ptr!=None:
            if count<=zerosCount:
                ptr.val = 0
            else:
                ptr.val = 1
            count += 1
            ptr = ptr.next
            
        return headA
        
ll1 = LinkedList()

ll1.insertAtEnd(0)
ll1.insertAtEnd(1)

ll1.printList()  

sol1 = Solution()
ll1.head = sol1.solve2(ll1.head)     
ll1.printList()