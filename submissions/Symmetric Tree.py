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
        def group_by_row(lst):
            """returns the original list grouped so that each sublist 
            represents a level of the binary tree
            (such lenghts are powers of 2)"""
            list_lenghts = []
            while sum(list_lenghts) < len(lst):
                list_lenghts.append(
                    2**len(list_lenghts)
                )

            grouped = []

            while lst:
                grouped.append([])
                while len(grouped[-1]) < list_lenghts[0] and lst:
                    grouped[-1].append(lst.pop(0))
                list_lenghts.pop(0)

            return grouped

        def is_list_symmetric(lst):
            """tests if a simple list is symmetric"""
            if len(lst) > 1:
                while len(lst) > 1:
                    if lst[0] != lst[-1]:
                        return False
                    lst = lst[1:-1]

            return True

        def is_grouped_list_symmetric(lst):
            """tests if all the sub-lists are symmetric"""
            for sublist in lst:
                if not is_list_symmetric(sublist):
                    return False
            return True

        current_node = root
        to_visit = [current_node]
        nodes_tuples = []

        while to_visit:
            current_node = to_visit.pop(0)

            val = current_node.val

            if current_node.left:
                left = current_node.left.val
                to_visit.append(current_node.left)
            else:
                left = None

            if current_node.right:
                right = current_node.right.val
                to_visit.append(current_node.right)
            else:
                right = None

            nodes_tuples.append((val, left, right))

        values = [node_tuple[0] for node_tuple in nodes_tuples]

        grouped_by_row = group_by_row(values)

        return is_grouped_list_symmetric(grouped_by_row)
