class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        stop = len(nums)-1
        while start <= stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= target < nums[mid]:
                stop = mid-1
            elif nums[mid] < target <= nums[stop]:
                start = mid+1
            elif nums[mid] > nums[stop]:
                start = mid+1
            else:
                stop = mid-1
        return -1
