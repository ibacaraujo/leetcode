class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        unsorted_nums = nums.copy()
        nums.sort()
        subarray_indices = []
        for i in range(len(nums)):
            if unsorted_nums[i] != nums[i]:
                subarray_indices.append(i)
        if len(subarray_indices) == 0:
            return 0
        return max(subarray_indices)-min(subarray_indices)+1
