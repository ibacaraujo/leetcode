class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        first = dict()
        last = dict()
        for i, item in enumerate(nums):
            if nums[i] not in first: first[item] = i 
            last[item] = i
            d[item] = d.get(item, 0) + 1
            
        shortest = len(nums)
        degree = max(d.values())
        for item in d:
            if d[item] == degree:
                shortest = min(shortest, last[item] - first[item] + 1)
        return shortest
