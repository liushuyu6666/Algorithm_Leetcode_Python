from typing import Optional, List


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insertWord(word)

    def search(self, word: str) -> bool:
        return self.trie.search_dfs(word, 0, self.trie.root)


class TrieNode:
    def __init__(self):
        self.child: List[Optional[TrieNode]] = [None] * 26
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            asc = ord(w) - ord('a')
            if curr.child[asc]:
                curr = curr.child[asc]
            else:
                curr.child[asc] = TrieNode()
                curr = curr.child[asc]
        curr.isWord = True

    def search_dfs(self, word: str, index: int, curr: Optional[TrieNode]) -> bool: # .ad
        if not curr:
            return False
        if index == len(word):
            return curr.isWord

        curr_char = word[index]
        if curr_char != '.':
            asc = ord(curr_char) - ord('a')
            return self.search_dfs(word, index + 1, curr.child[asc])
        else:
            for i in range(26):
                if self.search_dfs(word, index + 1, curr.child[i]):
                    return True
            return False
