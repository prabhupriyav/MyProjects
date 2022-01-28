class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            l3 = nums1+nums2
            l3.sort()
            mid = len(l3)
            if mid%2 == 0:
                mid  = int(mid/2)
                last = (l3[mid] + l3[mid - 1]) / 2
            else:
                mid = int(mid/2)
                last = l3[mid]
            return last
