# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # we will start of with dummy pointing to head 
        dummy = ListNode(0 , head)
        group_prev = dummy 

        #while list is present, iterate and find the kth position 
        while True :
            kth = group_prev
            for _ in range(k) :
                kth = kth.next 

                #if there are less than k nodes then leave it as it is 
                if not kth :
                    return dummy.next 
            

            #a vriable to point to begining of next group 
            group_next = kth.next 

            #reverse the group 
            prev = group_next 
            curr = group_prev.next #points to 1st element in LL

            while curr != group_next :
                next = curr.next 
                curr.next = prev
                prev = curr
                curr = next 
            

            #connect the reversed list with the rest of the list 
            old_start = group_prev.next 
            group_prev.next = kth
            group_prev = old_start



        