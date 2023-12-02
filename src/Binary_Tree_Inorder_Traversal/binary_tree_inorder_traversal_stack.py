from typing import Optional, List

from src.Binary_Tree_Inorder_Traversal.TreeNode import TreeNode


class BinaryTreeInorderTraversalStack:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        traversal = []

        curr = root
        while curr is not None or len(stack) > 0:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                traversal.append(curr.val)
                curr = curr.right

        return traversal
