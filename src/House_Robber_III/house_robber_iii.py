from functools import cache
from typing import Optional

from src.House_Robber_III.TreeNode import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.best_robbery_dfs(root)

    @cache
    def best_robbery_dfs(self, curr: TreeNode) -> int:
        if curr is None:
            return 0

        if curr.left is None and curr.right is None:
            return curr.val

        # curr.left is not None
        if curr.right is None:
            rob_curr: int = curr.val + self.best_robbery_dfs(curr.left.left) + self.best_robbery_dfs(curr.left.right)
            skip_curr: int = self.best_robbery_dfs(curr.left)
            return max(rob_curr, skip_curr)

        # curr.right is not None
        if curr.left is None:
            rob_curr: int = curr.val + self.best_robbery_dfs(curr.right.left) + self.best_robbery_dfs(curr.right.right)
            skip_curr: int = self.best_robbery_dfs(curr.right)
            return max(rob_curr, skip_curr)

        if curr.left is not None and curr.right is not None:
            rob_curr: int = curr.val + self.best_robbery_dfs(curr.left.left) + self.best_robbery_dfs(
                curr.left.right) + self.best_robbery_dfs(curr.right.left) + self.best_robbery_dfs(curr.right.right)
            skip_curr: int = self.best_robbery_dfs(curr.left) + self.best_robbery_dfs(curr.right)
            return max(rob_curr, skip_curr)