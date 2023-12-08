from typing import Optional

from src.Balanced_Binary_Tree.TreeNode import TreeNode


def get_depth(root: Optional[TreeNode]) -> (int, bool):
    if not root:
        return 0, True

    left_depth, left_balanced = get_depth(root.left)
    right_depth, right_balanced = get_depth(root.right)

    curr_depth: int = max(left_depth, right_depth) + 1
    curr_balanced: bool = abs(left_depth - right_depth) <= 1
    return curr_depth, curr_balanced & left_balanced & right_balanced


class BalancedBinaryTreeRecursion:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        root_depth, root_balanced = get_depth(root)

        return root_balanced
