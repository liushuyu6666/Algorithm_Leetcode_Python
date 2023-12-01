import unittest

from src.Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.construct_binary_tree_from_inorder_and_postorder_traversal import \
    ConstructBinaryTreeFromInorderAndPostorderTraversal
from src.Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.TreeNode import TreeNode


class TestConstructBinaryTree(unittest.TestCase):
    def test_construct_binary_tree_from_inorder_and_postorder_traversal(self):
        constructor = ConstructBinaryTreeFromInorderAndPostorderTraversal()

        expect_root = TreeNode(3)
        expect_root.left = TreeNode(9)
        expect_root.right = TreeNode(20, TreeNode(15), TreeNode(7))

        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        actual_root = constructor.buildTree(inorder, postorder)

        self.assertEqual(actual_root.val, expect_root.val)
        self.assertEqual(actual_root.left.val, expect_root.left.val)
        self.assertEqual(actual_root.right.left.val, expect_root.right.left.val)
        self.assertEqual(actual_root.right.right.val, expect_root.right.right.val)
        self.assertEqual(actual_root.right.val, expect_root.right.val)


if __name__ == "__main__":
    unittest.main()
