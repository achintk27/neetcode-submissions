# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # we can create a dummy node poiting to 1st node 
        #create new node whose value is 0 and next points to head 
        dummy = ListNode(0,head) # dummy ---> 1 ----> 2 ....
        slow = dummy
        fast = dummy

        # we first move fast to the node that needs to be removed 
        for _ in range(n + 1):
            fast = fast.next

        #move both until fast = None , this moves till slow = node - 1 of what we wanna remove 
        while fast : 
            slow = slow.next 
            fast = fast.next

        #This points slow to the node after what we wanna skip
        slow.next = slow.next.next
        
        return dummy.next
            




        
        