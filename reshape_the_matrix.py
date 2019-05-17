class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        reshaped = [[0 for col in range(c)] for row in range(r)]
        nums_array = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                nums_array.append(nums[i][j])
        k = 0
        for i in range(r):
            for j in range(c):
                reshaped[i][j] = nums_array[k]
                k += 1
        return reshaped
        
