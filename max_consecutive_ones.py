class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        if 0 not in nums:
            return len(nums)
        if 1 not in nums:
            return 0
        ones_count = 0
        consecutive_ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones_count += 1
                if i == (len(nums)-1):
                    consecutive_ones.append(ones_count)
            else:
                if ones_count > 0:
                    consecutive_ones.append(ones_count)
                ones_count = 0
        return max(consecutive_ones)
