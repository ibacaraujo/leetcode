import itertools

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #three = []
        #three_sum = []
        #three_sum_closest = -1
        #for combination in itertools.combinations(nums, 3):
        #    three.append(combination)
        #    three_sum.append(sum(combination))
        #subtractions = [abs(x - target) for x in three_sum]
        #index = subtractions.index(min(subtractions))
        #return three_sum[index]
        nums = sorted(nums)
        r = float('inf')
        for c in range(len(nums)-2):
            i, j = max(c+1, 
                       bisect.bisect_left(nums, 
                                          target-nums[len(nums)-1]-nums[c],
                                          c+1,
                                          len(nums)-1)-1), len(nums)-1
            while r != target and i < j:
                s = nums[c] + nums[i] + nums[j]
                r, i, j = min(r, s, key=lambda x: abs(x-target)), \
                          i + (s < target), \
                          j - (s > target)
        return r
            
