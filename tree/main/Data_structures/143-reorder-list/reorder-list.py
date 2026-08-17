# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second=slow.next
        prev = slow.next = None

        while second:
            nxt= second.next
            second.next = prev
            prev = second
            second = nxt

        curr_start, curr_end = head, prev
        while curr_end:
            temp1,temp2 = curr_start.next,curr_end.next
            curr_start.next = curr_end
            curr_end.next = temp1
            curr_start,curr_end = temp1,temp2


            
        