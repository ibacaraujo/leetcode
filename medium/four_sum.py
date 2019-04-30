class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set()
        d = dict()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pair_sum = nums[i]+nums[j]
                if pair_sum in d:
                    d[pair_sum].append((i,j))
                else:
                    d[pair_sum] = [(i,j)]
        
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:
                    for (k,l) in list2:
                        if i!=k and i!=l and j!=k and j!=l:
                            quadruplet = [nums[i], nums[j], nums[k], nums[l]]
                            quadruplet.sort()
                            result.add(tuple(quadruplet))
        return list(result)
