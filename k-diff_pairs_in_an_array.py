class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #num_pairs = 0
        #pairs = []
        #for i in range(len(nums)-1):
        #    for j in range(i+1, len(nums)):
        #        if (nums[i], nums[j]) not in pairs and (nums[j], nums[i]) not in pairs:
        #            print(nums[i], nums[j])
        #           if abs(nums[i] - nums[j]) == k:
        #                num_pairs += 1
        #                pairs.append((nums[i], nums[j]))
        #return num_pairs
        nums.sort()
        pairs = []
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                pairs.append((d[nums[i]], nums[i]))
            d[nums[i]+k] = nums[i]
        return len(set(pairs))
