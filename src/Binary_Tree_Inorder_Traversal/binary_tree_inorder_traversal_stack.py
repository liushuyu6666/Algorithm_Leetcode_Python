from typing import Optional, List

from src.Binary_Tree_Inorder_Traversal.TreeNode import TreeNode


class BinaryTreeInorderTraversalStack:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack: List[TreeNode] = []
        traversal: List[int] = []

        curr = root
        while curr or len(stack) > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                traversal.append(curr.val)
                curr = curr.right

        return traversal
