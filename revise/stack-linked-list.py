from linked_list import LinkedList

class Stack:
    
    def __init__(self):
        ll1 = LinkedList()
        self.stk = ll1
        self.stkSize = 0
    
    def push(self, val):
        self.stk.insertAtStart(val)
        self.stkSize += 1
        
    def pop(self):
        head = self.stk.head
        if head==None:
            return
        
        ptr = head.next
        del head
        self.stkSize -= 1
        self.stk.head = ptr
    
    def top(self):
        if self.stk.head==None:
            return 
        
        return self.stk.head.val
    
    def isEmpty(self):
        if self.stkSize == 0:
            return True
        return False
    
    def sizeOfStack(self):
        return self.stkSize
    
stk1 = Stack()
for i in range(5):
    stk1.push(i)
    
print(stk1.top())

stk1.pop()
        
print(stk1.top())
print(stk1.isEmpty())
print(stk1.sizeOfStack())