class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.isEnd = True

    def search(self, word):
        
        def dfs(node, i):
            # Base case
            if i == len(word):
                return node.isEnd
            
            ch = word[i]
            
            # Case 1: normal character
            if ch != '.':
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)
            
            # Case 2: wildcard '.'
            else:
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
        
        return dfs(self.root, 0)