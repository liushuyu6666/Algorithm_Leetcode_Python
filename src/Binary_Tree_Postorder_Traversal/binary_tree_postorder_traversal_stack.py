from typing import Optional, List

from src.Binary_Tree_Postorder_Traversal.TreeNode import TreeNode


class BinaryTreePreorderTraversalStack:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack: List[TreeNode] = []  # stack 1
        loading: List[TreeNode] = []  # stack 2
        traversal: List[int] = []

        stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            loading.append(curr)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        while len(loading) > 0:
            traversal.append(loading.pop().val)

        return traversal
