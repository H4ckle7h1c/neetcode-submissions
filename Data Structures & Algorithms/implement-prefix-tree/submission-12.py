class Node: 
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter] 
        
        node.end = True

        
    def search(self, word: str) -> bool:
        node = self.root
        if node is None: 
            return False

        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
    
        return node.end 
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        if node is None:
            return False

        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return False
        
        return True 


        
        