#https://www.interviewbit.com/problems/reverse-linked-list/

# Reverse a linked list. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL,
# return 5->4->3->2->1->NULL.
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

from linked_list import LinkedList

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reverseList(self, A):
        headA = A
        
        if headA.next==None:
            return headA
        isFirstNode = True
        
        ptr1 = headA
        ptr2 = ptr1.next
        ptr3 = ptr2.next
        
        while ptr1.next!=None:
            #print(ptr1.val, ptr2.val, ptr3.val)
            if isFirstNode:
                ptr1.next = None
                isFirstNode = False
            
            
            if ptr2.next==None:
                ptr3 = ptr2
                
            ptr2.next = ptr1
            ptr1 = ptr2
            
            if ptr1==ptr3:
                return ptr1
            
            if ptr3!=None:
                ptr2 = ptr3
            if ptr3.next!=None:
                ptr3 = ptr3.next
            else:
                ptr3 = None
            
        
ll1  = LinkedList()        
for i in range(5):
    ll1.insertAtStart(i)

ll1.printList()

sol1 = Solution()


ll1.head = sol1.reverseList(ll1.head)
ll1.printList()

            