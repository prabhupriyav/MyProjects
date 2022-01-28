class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        output = []
        nums.sort()
        len_nums = len(nums)-k
        return nums[len_nums]
