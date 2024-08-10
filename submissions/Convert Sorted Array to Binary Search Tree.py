# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nodes = [TreeNode(val) for val in nums]

        def split(array):
            if len(array) > 0:
                midpoint = int(len(array)/2)
                mid = array[midpoint]
                left = array[:midpoint]
                if not left:
                    left = None
                right = array[midpoint+1:]
                if not right:
                    right = None
                return (left, mid, right)
            else:
                return (None, None, None)

        def set_children_of_mid(array):
            left, mid, right = split(array)
            if mid is not None:
                if left is not None:
                    mid.left = set_children_of_mid(left)
                if right is not None:
                    mid.right = set_children_of_mid(right)
            return mid

        return set_children_of_mid(nodes)
