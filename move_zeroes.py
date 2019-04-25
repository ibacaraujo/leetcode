class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[i] == 0:
                tmp = nums.pop(i)
                nums.append(tmp)
            else:
                i += 1
            j += 1
        return nums
