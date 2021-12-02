# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        #fast 快慢指针: 快2格 慢 1格
        #slow
        fast=slow=head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow