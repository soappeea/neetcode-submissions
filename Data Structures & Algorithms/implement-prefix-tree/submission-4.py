class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode() # initialize prefix tree obj

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            i = ord(c) - ord('a') # find char index
            if cur.children[i] == None:
                cur.children[i] = TrieNode() # add char to prefix tree
            cur = cur.children[i]
        cur.endOfWord = True # end of word

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        
        return cur.endOfWord # only a word if ended
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True
        
        
        