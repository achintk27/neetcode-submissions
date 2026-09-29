# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #We solve this by taking 2 lists at a time and go on until all lists are merged 

        #check if there are any lists 
        if not lists :
            return None 

        
        #Merge 2 sorted LL 
        def merge2(l1 , l2) :
            dummy = ListNode(0)
            tail = dummy 

            while l1 and l2 : 
                if l1.val <= l2.val :
                    tail.next = l1 
                    l1 = l1.next 
                else :
                    tail.next = l2
                    l2 = l2.next 
                tail = tail.next
                
            #in the end there will be 1 val remaining 
            if l1 :
                tail.next = l1
            else :
                tail.next = l2 
                
            return dummy.next 

        #Now we need to write a function that goes on and comapres all LL 2 lists at a time
        while len(lists) > 1 :
            merged = []
        
        #take 2 lists at a time 
            for i in range(0 , len(lists), 2)  :
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None 

                #call the merge2 function 
                merged.append(merge2(l1,l2))
        
            lists = merged
        
        return lists[0]

        














