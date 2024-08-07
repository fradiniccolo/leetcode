# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # if node and node.next:
        #     node_to_be_replaced_with = node.next
        #     node.val = node_to_be_replaced_with.val
        #     node.next = node_to_be_replaced_with.next
        #     del node_to_be_replaced_with

        if node.next:
            node.val = node.next.val
            node.next = node.next.next