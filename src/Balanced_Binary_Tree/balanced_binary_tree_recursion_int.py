from typing import Optional

from src.Balanced_Binary_Tree.TreeNode import TreeNode


def get_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_depth = get_depth(root.left)

    if left_depth == -1:
        return -1

    right_depth = get_depth(root.right)

    if right_depth == -1:
        return -1

    return max(left_depth, right_depth) + 1 if abs(left_depth - right_depth) <= 1 else -1


class BalancedBinaryTreeRecursion:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return get_depth(root) != -1