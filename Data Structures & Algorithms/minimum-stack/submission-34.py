class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min
        self.next = None 
        self.prev = None
class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, val)
            return 
        
        new_head = Node(val, val)

        if self.head.min < val:
            new_head.min = self.head.min
        
        self.head.next = new_head
        new_head.prev = self.head
        self.head = new_head

    def pop(self) -> None:
        if self.head is not None:
            self.head = self.head.prev

        

    def top(self) -> int:
        if self.head == None:
            return -1 
        
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.min
