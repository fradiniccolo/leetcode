# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        to_visit = {root: 1}    # {node: path_depth, ...}
        visited = {}            # {node: path_depth, ...}
        deepest_path = 1
        while to_visit:
            current = next(iter(to_visit))
            if current.left:
                to_visit[current.left] = to_visit[current]+1
            if current.right:
                to_visit[current.right] = to_visit[current]+1
            visited[current] = to_visit.pop(current)
            if visited[current] > deepest_path:
                deepest_path = visited[current]

        return deepest_path
