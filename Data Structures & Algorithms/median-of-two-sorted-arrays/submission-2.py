class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # intuition : merge them and the find middle - time completixy is more O(m+n)

        # Find the shorter array , label that as nums1 and perform binary search on that 
        if len(nums1) > len(nums2) :
            nums1 , nums2 = nums2 , nums1
        
        m = len(nums1)
        n = len(nums2)

        #caliculate how many elements will be on the left of the 2 arrays combined 
        left_size = (m+n+1) // 2 # floor division
        
        #Normal binary search , left = 0 , right = m 
        left = 0
        right = m

        #perform search
        while left <= right :

            #make the cuts to split each array into 2 halves 
            cut1 = (left + right) //2
            
            #whatever is remaning 
            cut2 = left_size - cut1


            #divide the array into left and right 
            left1 = nums1[cut1-1] if cut1 > 0 else float("-inf") 
            right1 = nums1[cut1] if cut1 < m else float("inf") 

            left2 = nums2[cut2-1] if cut2 > 0 else float("-inf") 
            right2 = nums2[cut2] if cut2 < n else float("inf") 

            #check if every value on combined left < every value on combined right
            if left1 <= right2 and left2 <= right1 :

                #calicluate median 
                #for odd total number of values 
                if (m + n) % 2 == 1 :
                    return max(left1,left2)
                
                #for even number of values 
                return (max(left1 ,left2) + min(right1,right2)) / 2

            if left1 > right2 :
                right = cut1 - 1 
            else :
                left = cut1 + 1 






