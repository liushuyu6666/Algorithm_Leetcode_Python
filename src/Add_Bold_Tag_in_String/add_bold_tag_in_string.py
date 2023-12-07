from typing import List


def find_word_in_string(s: str, word: str, overlap: List[bool]) -> None:
    length = len(word)
    find_index = s.find(word, 0)
    while find_index != -1:
        overlap[find_index: find_index + length] = [True] * length
        find_index = s.find(word, find_index + 1)


def add_bold_tag(s: str, overlap: List[bool]) -> str:
    overlap = [False] + overlap
    prev = False
    for i in range(len(overlap) - 1, -1, -1):
        # prev is False but curr overlap is True
        if not prev and overlap[i]:
            s = s[: i] + "</b>" + s[i:]
        # prev is True but curr overlap is False
        elif prev and not overlap[i]:
            s = s[:i] + "<b>" + s[i:]
        prev = overlap[i]

    return s


class AddBoldTagInString:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        overlap = [False] * len(s)

        for word in words:
            find_word_in_string(s, word, overlap)

        return add_bold_tag(s, overlap)
