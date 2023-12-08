from typing import Optional, List

from src.Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked_List.Node import Node


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        stack: List[Node] = []
        curr = root
        prev, head = None, None

        while curr or len(stack) > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if not prev:
                    head = curr
                else:
                    prev.right = curr
                    curr.left = prev
                prev = curr

                curr = curr.right

        prev.right = head
        head.left = prev

        return head

