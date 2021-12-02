# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         res = None
#         while head:
#             oldnext = head.next
#             head.next = res
#             res = head
#             head = oldnext
#         return res
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversedList = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedList
