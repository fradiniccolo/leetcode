# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def max_subtree_val(node):

            current_node = node
            to_visit = [current_node]
            max_val_found = None

            while to_visit:

                current_node = to_visit.pop(0)
                if current_node.left:
                    to_visit.append(current_node.left)
                if current_node.right:
                    to_visit.append(current_node.right)

                if max_val_found is None:
                    max_val_found = current_node.val
                elif current_node.val > max_val_found:
                    max_val_found = current_node.val

            return max_val_found

        def min_subtree_val(node):

            current_node = node
            to_visit = [current_node]
            min_val_found = None

            while to_visit:

                current_node = to_visit.pop(0)
                if current_node.left:
                    to_visit.append(current_node.left)
                if current_node.right:
                    to_visit.append(current_node.right)

                if min_val_found is None:
                    min_val_found = current_node.val
                elif current_node.val < min_val_found:
                    min_val_found = current_node.val

            return min_val_found

        def validate_subtree(node):
            pass

        if min_subtree_val(root.left) >= root.left:
            return False
        if max_subtree_val(root.right) <= root.right:
            return False
        if not validate_subtree(root):
            return False
        return True
