# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        current = head

        visited_vals = set()

        while current:
            if current not in visited_vals:
                visited_vals.add(current)
                current = current.next
            else:
                return True

        return False
