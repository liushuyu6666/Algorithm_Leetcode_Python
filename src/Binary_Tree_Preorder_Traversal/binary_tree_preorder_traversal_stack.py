from typing import Optional, List

from src.Binary_Tree_Preorder_Traversal.TreeNode import TreeNode


class BinaryTreePreorderTraversalStack:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack: List[TreeNode] = []
        traversal: List[int] = []

        stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            traversal.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return traversal

