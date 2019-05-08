class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subsets.append([])
        for num in nums:
            for i in range(len(subsets)):
                print(subsets[i] + [num])
                subsets.append(subsets[i] + [num])
        return subsets
