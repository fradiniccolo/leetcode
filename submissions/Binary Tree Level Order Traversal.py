# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        current_node = root
        to_visit = [(0, current_node)]

        values = {}
        while any(to_visit):
            depth, current_node = to_visit.pop(0)
            if current_node:
                if depth not in values.keys():
                    values[depth] = []
                values[depth].append(current_node.val)
                to_visit.append((depth+1, current_node.left))
                to_visit.append((depth+1, current_node.right))

        return list(values.values())
