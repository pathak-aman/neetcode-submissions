# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, low, high):
            if not root:
                return True

            if not (low < root.val < high):
                return False

            left_valid = traverse(root.left, low, root.val)
            right_valid = traverse(root.right, root.val, high)

            return left_valid and right_valid
        return traverse(root, -float("inf"), float("inf"))


