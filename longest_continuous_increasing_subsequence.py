class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = []
        count = 0
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
                if i == len(nums)-2:
                    count += 1
                    counts.append(count)
            else:
                count += 1
                counts.append(count)
                count = 0
        return max(counts)
