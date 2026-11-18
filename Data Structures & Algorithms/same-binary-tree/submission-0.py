# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(root_q, root_p):
            if root_q is None and root_p is None:
                return True
            elif (root_q is None and root_p) or (root_q and root_p is None):
                return False

            if root_q.val == root_p.val:
                same_l = traverse(root_q.left, root_p.left)
                same_r = traverse(root_q.right, root_p.right)

                if same_l == True and same_r == True:
                    return True
    
            return False

        return traverse(p,q)