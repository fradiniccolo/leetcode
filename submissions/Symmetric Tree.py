# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def are_specular(n1, n2):

            if n1 is None and n2 is None:
                # both None
                return True
            elif n1 is not None and n2 is not None:
                # neither None
                if n1.val != n2.val:
                    return False
                return are_specular(n1.left, n2.right) and are_specular(n1.right, n2.left)
            else:
                # only one None
                return False

        return are_specular(root.left, root.right)
