class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #count = 0
        #for i in range(len(nums)-1):
        #    if nums[i] > nums[i+1]:
        #        count += 1
        #if count > 1:
        #    return False
        #return True
        new1 = nums[:]
        new2 = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                new1[i] = nums[i+1]
                new2[i+1] = nums[i]
                break
        return new1 == sorted(new1) or new2 == sorted(new2)
