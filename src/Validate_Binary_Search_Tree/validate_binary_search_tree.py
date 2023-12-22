from typing import Optional

from src.Validate_Binary_Search_Tree.TreeNode import TreeNode


class ValidateBinarySearchTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidDFS(node: Optional[TreeNode], min_limit: Optional[int], max_limit: Optional[int]) -> bool:
            if not node:
                return True

            if min_limit is not None and node.val <= min_limit:
                return False
            if max_limit is not None and node.val >= max_limit:
                return False

            return isValidDFS(node.left, min_limit, node.val) and isValidDFS(node.right, node.val, max_limit)

        return isValidDFS(root, None, None)

