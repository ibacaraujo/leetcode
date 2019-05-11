class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                break
        i = i - 1
        next_larger = [j for j in nums[i:] if j > nums[i]]
        if not next_larger:
            nums.reverse()
        else:
            min_larger = min(next_larger)
            idx = nums[i:].index(min_larger) + i
            nums[i], nums[idx] = nums[idx], nums[i]
            nums[:] = nums[:i+1] + sorted(nums[i+1:])
