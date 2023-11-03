from functools import cache
from typing import Optional

from src.House_Robber_III.TreeNode import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def rob_or_skip_dfs(curr: Optional[TreeNode]) -> (int, int):
            if not curr:
                return 0, 0

            left_max = rob_or_skip_dfs(curr.left)
            right_max = rob_or_skip_dfs(curr.right)

            return curr.val + left_max[1] + right_max[1], max(left_max) + max(right_max)

        return max(rob_or_skip_dfs(root))

    # (the max value of robbing this house, the max value of skipping this house)
    def rob_or_skip_dfs(self, curr: TreeNode) -> (int, int):
        if not curr:
            return 0, 0

        left_max = self.rob_or_skip_dfs(curr.left)
        right_max = self.rob_or_skip_dfs(curr.right)

        return curr.val + left_max[1] + right_max[1], max(left_max) + max(right_max)