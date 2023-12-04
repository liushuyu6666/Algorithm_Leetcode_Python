from typing import Optional, List

from src.Binary_Tree_Postorder_Traversal.TreeNode import TreeNode


class BinaryTreePreorderTraversalRecursion:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal: List[int] = []

        def postorder(curr: Optional[TreeNode]):
            if curr:
                postorder(curr.left)
                postorder(curr.right)
                traversal.append(curr.val)

        postorder(root)

        return traversal

