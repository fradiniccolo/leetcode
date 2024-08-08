# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        current_node= root
        to_visit = [current_node]
        nodes_val = []
        
        while to_visit:

            current_node = to_visit.pop(0)
            # if not current_node:
            #     continue

            if current_node.left:
                to_visit.append(current_node.left)
            if current_node.right:
                to_visit.append(current_node.right)
            
            if not nodes_val:
                nodes_val.append(current_node)
            elif 