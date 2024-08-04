# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # single node case
        if head.next == None:
            del head
            return None

        # find node
        buffer = []
        buffer.append(head)
        while True:
            next_node = buffer[-1].next
            if next_node is not None:
                buffer.append(next_node)
            else:
                if n != 1:
                    # delete middle node
                    sel_node = buffer[-n]
                    sel_node.val = sel_node.next.val
                    sel_node.next = sel_node.next.next
                else:
                    # delete last node
                    sel_node = buffer[-n-1]
                    sel_node.next = None
                break

        return head
