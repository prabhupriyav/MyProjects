class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = 0
        j = 0
        kth_dict = {}
        nums.sort()
        for i in nums:
            count = nums.count(i)
            kth_dict[i] = count
        while j != k:
            max_val = max(kth_dict,key = kth_dict.get)
            output.append(max_val)
            kth_dict.pop(max_val)
            j+=1    
        if len(nums) <= k:
            return nums
        else:
            return set(output)
