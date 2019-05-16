class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([min(x,y) for x,y in zip(nums[::2], nums[1::2])])
