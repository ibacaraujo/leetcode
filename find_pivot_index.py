class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums) == 0:
        #    return -1
        #if sum(nums[1:]) == 0:
        #    return 0
        #for i in range(1, len(nums)):
        #    if sum(nums[:i]) == sum(nums[i+1:]):
        #        return i
        #return -1
        S = sum(nums)
        l_sum = 0
        for i in range(len(nums)):
            if l_sum == (S - l_sum - nums[i]):
                return i
            l_sum += nums[i]
        return -1
