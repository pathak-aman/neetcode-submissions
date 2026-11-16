# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(root):
            if not root:
                return root
            invert(root.left)
            invert(root.right)
            root.left, root.right = root.right, root.left
            return root

        return invert(root)
        

                        #         f(1)
                        #     f(3)       f(2)
                        # f(7)   f(6).  f(5) f(4)
                        





        