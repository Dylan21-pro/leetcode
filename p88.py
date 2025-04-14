class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m+n == 1:
            if m == 0:
                nums1[0]=nums2[0]
        else:
            arr = nums1[:m]
            ct1 = 0
            ct2 = 0
            while ct1 < m and ct2 < n:
                if arr[ct1] > nums2[ct2]:
                    nums1[ct1+ct2] = nums2[ct2]
                    ct2 += 1
                elif arr[ct1] <= nums2[ct2]:
                    nums1[ct1+ct2] = arr[ct1]
                    ct1 += 1 

            while ct1 < m:
                nums1[ct1+ct2] = arr[ct1]
                ct1 += 1

            while ct2 < n:
                nums1[ct1+ct2] = nums2[ct2]
                ct2 += 1

                

                 
        
