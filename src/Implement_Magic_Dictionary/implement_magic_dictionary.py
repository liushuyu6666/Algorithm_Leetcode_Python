from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.child: List[Optional[TrieNode]] = [None] * 26
        self.suffix: List[str] = []
        self.isWord: bool = False

class MagicDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:

            curr = self.trie
            for i in range(len(word)):
                suffix = word[i:]
                curr.suffix.append(suffix)
                idx = ord(word[i]) - ord('a')
                if not curr.child[idx]:
                    curr.child[idx] = TrieNode()
                curr = curr.child[idx]
            curr.suffix.append('')

    def search(self, searchWord: str) -> bool:
        def oneChange(index: int, curr: Optional[TrieNode]) -> bool:
            if not curr:
                return False
            if index == len(searchWord):
                return False

            suffix = searchWord[index + 1:]
            asc = ord(searchWord[index]) - ord('a')
            for i in range(26):
                if curr.child[i] and i != asc and suffix in curr.child[i].suffix:
                    return True
            return False

        curr = self.trie
        for i in range(len(searchWord)):
            if oneChange(i, curr):
                return True
            else:
                idx = ord(searchWord[i]) - ord('a')
                if not curr.child[idx]:
                    return False
                curr = curr.child[idx]
        return False





