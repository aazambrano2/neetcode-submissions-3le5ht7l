# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        seen = set()
        def help(head,seen):
            if head.next in seen:
                return True
            if not head.next:
                return False
            seen.add(head)
            return help(head.next,seen)
        return help(head,seen)
        