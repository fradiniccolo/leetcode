# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self.next:
            return f"ListNode({self.val}->{self.next.val})"
        else:
            return f"ListNode({self.val}->None)"
        
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node_to_delete = node.next
            node.val = node_to_delete.val
            node.next = node_to_delete.next
            del node_to_delete

head = [4,5,1,9]

for index, val in enumerate(head):
    head[index] = ListNode(val)

for index, val in enumerate(head):
    if index < len(head)-1:
        head[index].next = head[index+1]

for item in head:
    print(item)

test = Solution()
test.deleteNode(
    head[1]
)


print()
for item in head:
    print(item)
