# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #L1 = "321" --- 1---> 2----> 3
        #L2 = "654" --- 4---> 5----> 6
        #output = [ "5", "7", "9"]

        # if its 2 digit number after adding , we use carry 

        # we can use dummy , carry 
        dummy = ListNode(0)
        tail = dummy 
        carry = 0 

        #we need to point to the digits 

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0 

            total = digit1 + digit2 + carry 

            # we need the remainder for carry
            digit = total % 10 
            carry = total // 10 

            #We create a new node with the digit and place it after tail. 
            tail.next = ListNode(digit) 
            tail = tail.next 

            if l1 :
                l1 = l1.next 
            if l2 :
                l2  = l2.next 

        return dummy.next


