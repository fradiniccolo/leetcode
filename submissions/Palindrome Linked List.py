# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        from collections import deque
        
        # create record of values
        current_node = head
        record = deque()
        while current_node:
            record.append(current_node.val)
            current_node = current_node.next

        # check if palindrome
        while len(record) > 1:
            if record[0] == record[-1]:
                record.pop()
                record.popleft()
            else:
                return False

        return True
