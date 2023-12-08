from typing import Optional

from src.Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked_List.Node import Node


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        prev, head = None, None

        def inorder(curr: Optional[Node]):
            nonlocal prev, head  # declare prev and head as a nonlocal variable
            if not curr:
                return

            # traverse its left subtree
            inorder(curr.left)

            # When the code reaches this point, the left subtree of the current node has been fully traversed. Given that the `inorder` function retrieves the right subtree at the end, it is imperative that the `prev` variable points to the last node of the right subtree of `curr.left`.
            if not prev:
                head = curr
            else:
                curr.left = prev
                prev.right = curr
            prev = curr

            # traverse its right subtree
            inorder(curr.right)

        inorder(root)
        prev.right = head
        head.left = prev

        return head
