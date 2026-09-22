class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min
        self.next = None 
        self.prev = None
class MinStack:

    def __init__(self):
        self.min = None
        self.head = None

    def push(self, val: int) -> None:
        if self.min == None:
            self.min = val 
        elif val < self.min:
            self.min = val
        
        node = Node(val, self.min)
        
        if self.head == None:
            self.head = node
            return 

        self.head.next = node
        node.prev = self.head
        self.head = node
        print('pushing',node.val,'new head', self.head.val, 'new min', self.head.min)

    def pop(self) -> None:
        if self.head == None:
            return

        if self.head.prev is None: 
            # Empty Stack
            self.head = None
            self.min = None
            print('stack empty')
            return
        
        self.min = self.head.prev.min
        self.head = self.head.prev
        print('poped', self.head.val,'new min', self.min)

        

    def top(self) -> int:
        if self.head == None:
            return -1 
        
        return self.head.val
        

    def getMin(self) -> int:
        return self.min
