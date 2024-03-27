class Stack:
    
    
    def __init__(self):
        self.stk = []
        
    def push(self, val):
        self.stk.append(val)
        
    def pop(self):
        if len(self.stk)>0:
            return self.stk.pop()
    
    def top(self):
        if len(self.stk)>0:
            n = len(self.stk)
            return self.stk[n-1]   
        
    def isEmpty(self):
        if len(self.stk)==0:
            return True
        return False
    
    def sizeOfStack(self):
        return len(self.stk)         
                
stk1 = Stack()
for i in range(5):
    stk1.push(i)
    
print(stk1)
    
print(stk1.pop())
print(stk1.pop())

print(stk1.top())

stk1.push(10)

print(stk1.top())

print(stk1.isEmpty())
print(stk1.sizeOfStack())