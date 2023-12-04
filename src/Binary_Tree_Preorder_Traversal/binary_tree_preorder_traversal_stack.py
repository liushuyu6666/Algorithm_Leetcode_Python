from typing import Optional, List

from src.Binary_Tree_Preorder_Traversal.TreeNode import TreeNode


class BinaryTreePreorderTraversalStack:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack: List[TreeNode] = []
        traversal: List[int] = []

        curr = root
        while curr or len(stack) > 0:
            if curr:
                traversal.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
            curr = stack.pop()

        return traversal

