class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return
        nums_set = set(nums)
        nums_list = list(range(1, len(nums)+1))
        return list(set(nums_list)-nums_set)
