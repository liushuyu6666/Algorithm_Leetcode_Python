import unittest
from src.Validate_Binary_Search_Tree.validate_binary_search_tree import ValidateBinarySearchTree
from src.Validate_Binary_Search_Tree.TreeNode import TreeNode


class TestValidateBinarySearchTree(unittest.TestCase):
    def test_validate_binanry_search_tree(self):
        solution = ValidateBinarySearchTree()

        root = TreeNode(0, None, TreeNode(-1, None, None))
        self.assertEqual(solution.isValidBST(root), False)