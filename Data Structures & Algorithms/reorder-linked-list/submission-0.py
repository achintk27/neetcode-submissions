# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # We solve it in 3 steps 
        # 1. find the middle 
        # 2. reverse the second half 
        # join the 2 in required order 

        # lets start with 2 pointers fast and slow to find middle 
        slow = fast = head

        # When fast.next or fast.next.next = None , the node that slow is pointing to is the lst element of 1st half 
        while fast.next and fast.next.next :
            slow = slow.next 
            fast = fast.next.next 

        #When fast.next or fast.next.next = None 
        second_half = slow.next 
        slow.next = None # This breaks the linked list into 2 halves 


        # now we reverse the 2nd half 
        previous = None 
        while second_half :
            next_node = second_half.next
            second_half.next = previous 
            previous = second_half
            second_half = next_node 
        

        # We now join them together in the required order 

        second_half = previous # head of 2nd half 
        first = head 

        while second_half : 

            first_next = first.next 
            second_next = second_half.next 

            first.next = second_half
            second_half.next = first_next

            first = first_next
            second_half = second_next


