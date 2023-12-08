import unittest
from src.Balanced_Binary_Tree.balanced_binary_tree_recursion_tuple import BalancedBinaryTreeRecursion
from src.Balanced_Binary_Tree.TreeNode import TreeNode


class TestBalancedBinaryTreeRecursion(unittest.TestCase):
    def test_balanced_binary_tree_recursion_tuple(self):
        balanced = BalancedBinaryTreeRecursion()

        left_bottom = TreeNode(3, TreeNode(4), TreeNode(4))
        left = TreeNode(2, left_bottom, TreeNode(3))
        right = TreeNode(2)
        root = TreeNode(1, left, right)

        self.assertEqual(balanced.isBalanced(root), False)