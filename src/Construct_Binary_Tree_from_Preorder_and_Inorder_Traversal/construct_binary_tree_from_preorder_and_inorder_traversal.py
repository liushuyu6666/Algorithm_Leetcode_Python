from typing import List, Optional

from src.Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.TreeNode import TreeNode


def split_inorder(inorder: List[int], preorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not preorder:
        return None

    curr_val = preorder.pop(0)
    val_index = inorder.index(curr_val)
    curr_node = TreeNode(curr_val)
    left_inorder = inorder[0: val_index]
    right_inorder = inorder[val_index + 1:]
    curr_node.left = split_inorder(left_inorder, preorder)
    curr_node.right = split_inorder(right_inorder, preorder)

    return curr_node


class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return split_inorder(inorder, postorder)
