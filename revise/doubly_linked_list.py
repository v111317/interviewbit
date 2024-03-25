class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, val):
        node1 = Node(val)
        
        if self.head==None:
            self.head = node1
        else:
            ptr = self.head
            node1.right = ptr
            ptr.left = node1
            self.head = node1
        
        return

    def insertAtEnd(self, val):
        node1 = Node(val)
        
        if self.head==None:
            self.head = node1
            return
        
        ptr = self.head
        
        while ptr.right!=None:
            ptr = ptr.right
            
        ptr.right = node1
        node1.left = ptr
        return

    #if null list - insert at first position
    #if list small - insert at end
    def insertAtIndex(self, val, posn):
        node1 = Node(val)
        
        if self.head==None:
            self.head = node1
            return
        
        currIdx = 0
        ptr = self.head
        
        while ptr!=None and currIdx<posn:
            ptr = ptr.right
            currIdx += 1
            if ptr.right==None:
                ptr.right = node1
                node1.left = ptr
                return
        
        node1.right = ptr
        node1.left = ptr.left
        
        if ptr.left!=None:
            prev = ptr.left
            prev.right = node1
        
            ptr.left = node1
        
        if posn==0:
            ptr.left = node1
            self.head = node1
        
        return
        
        
    def printList(self):
        
        ptr = self.head
        while ptr!=None:
            print(ptr.val, " -> ", end="")
            ptr = ptr.right
        
        print("")
        return
        
        
    

ll1 = DoublyLinkedList()

# for i in range(5):
#     ll1.insertAtBegin(i)
    
# ll1.printList()


ll2 = DoublyLinkedList()

for i in range(5):
    ll2.insertAtEnd(i)
    
ll2.printList()

ll2.insertAtIndex(101, 0)
ll2.insertAtIndex(102, 20)
ll2.printList()
