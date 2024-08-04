# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        candidate1 = list1
        candidate2 = list2

        # find the head
        if not candidate1 and not candidate2:
            return
        elif not candidate2:
            head = candidate1
            candidate1 = candidate1.next
        elif not candidate1:
            head = candidate2
            candidate2 = candidate2.next
        elif candidate1.val <= candidate2.val:
            head = candidate1
            candidate1 = candidate1.next
        else:
            head = candidate2
            candidate2 = candidate2.next
        current = head

        # connect the other nodes
        while candidate1 or candidate2:
            if not candidate2:
                current.next = candidate1
                current = candidate1
                candidate1 = candidate1.next
            elif not candidate1:
                current.next = candidate2
                current = candidate2
                candidate2 = candidate2.next
            elif candidate1.val <= candidate2.val:
                current.next = candidate1
                current = candidate1
                candidate1 = candidate1.next
            else:
                current.next = candidate2
                current = candidate2
                candidate2 = candidate2.next

        return head
