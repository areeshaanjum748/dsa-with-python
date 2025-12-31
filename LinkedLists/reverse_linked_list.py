# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr_ptr, next_ptr, prev_ptr = None, None, None

        curr_ptr = head
        while(curr_ptr):
            next_ptr = curr_ptr.next
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr

        return prev_ptr
        
