class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            pos = ord(ch) - ord('a')
            if not temp.children[pos]:
                temp.children[pos] = TrieNode()
            temp = temp.children[pos]
        temp.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            pos = ord(ch) - ord('a')
            if curr.children[pos]:
                curr = curr.children[pos]
            else:
                return False
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            pos = ord(ch) - ord('a')
            if curr.children[pos]:
                curr = curr.children[pos]
            else:
                return False
        return True

        