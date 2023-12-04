from typing import Optional, List

from src.Binary_Tree_Preorder_Traversal.TreeNode import TreeNode


class BinaryTreePreorderTraversalRecursion:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal: List[int] = []

        def preorder(node: Optional[TreeNode]) -> None:
            if node:
                traversal.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        return traversal

