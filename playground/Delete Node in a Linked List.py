# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        if self.next:
            return f"ListNode({self.data}->{self.next.val})"
        else:
            return f"ListNode({self.data}->None)"
        
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

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        
    def add(self, node_data):
        new_head = ListNode(node_data, self.head)
        self.head = new_head
        self.size += 1

    def __str__(self):
        string = []
        pointer = self.head
        while pointer.next:
            string.append(pointer.data)
            pointer = pointer.next
        string = ' -> '.join(string)
        return string


linked_list_list = [4,5,1,9]

linked_list = LinkedList()
for item in linked_list_list:
    linked_list.add(ListNode(item))

print(linked_list)



# test = Solution()
# test.deleteNode(
#     head[1]
# )
# 
# 
# print()
# for item in head:
#     print(item)
# 