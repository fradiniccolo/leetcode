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

        def get_subtree_max(node):

            current_node = node
            to_visit = [current_node]
            max_val_found = None

            while to_visit:

                current_node = to_visit.pop(0)
                if not current_node:
                    continue

                if current_node.left:
                    to_visit.append(current_node.left)
                if current_node.right:
                    to_visit.append(current_node.right)

                if max_val_found is None:
                    max_val_found = current_node.val
                elif current_node.val > max_val_found:
                    max_val_found = current_node.val

            return max_val_found

        def get_subtree_min(node):

            current_node = node
            to_visit = [current_node]
            min_val_found = None

            while to_visit:

                current_node = to_visit.pop(0)
                if not current_node:
                    continue

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
            if node.left:
                if not node.val > get_subtree_max(node.left):
                    return False
            if node.right:
                if not node.val < get_subtree_min(node.right):
                    return False
            return True

        current_node = root
        to_visit = [current_node]

        while to_visit:

            current_node = to_visit.pop(0)

            if not validate_subtree(current_node):
                return False

            if current_node.left:
                to_visit.append(current_node.left)
            if current_node.right:
                to_visit.append(current_node.right)

        return True
