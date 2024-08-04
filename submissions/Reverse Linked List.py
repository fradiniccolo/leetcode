# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return
        
        current_node = head
        next_node = current_node.next
        current_node.next = None

        while next_node:

            # move one step
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next

            # re-wire
            current_node.next = previous_node

        return current_node
