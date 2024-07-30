# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"N-{self.val}"


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # ...
        
        return head

# test
head = [1, 2, 3, 4, 5]
n = 2

# build head
num_head = [item for item in head]
head = []
for val, next in zip([None] + num_head, num_head + [None]):
    if val:
        head.append(ListNode(val, next))

print(num_head)
print(head)

sol = Solution()
sol.removeNthFromEnd(head, n)

print(head)
