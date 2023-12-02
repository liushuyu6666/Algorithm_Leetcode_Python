from typing import Optional, List

from src.Binary_Tree_Inorder_Traversal.TreeNode import TreeNode


class BinaryTreeInorderTraversalStack:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal: List[int] = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node:
                inorder(node.left)
                traversal.append(node.val)
                inorder(node.right)

        inorder(root)

        return traversal

