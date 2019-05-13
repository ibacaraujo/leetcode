class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        stop = len(nums)-1
        while start <= stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                stop = mid - 1
        if start > stop:
            return [-1, -1]
        start = mid - 1
        stop = mid + 1
        while (start >= 0 and nums[start] == target):
            start = start - 1
        while (stop <= len(nums)-1 and nums[stop] == target):
            stop = stop + 1
        return [start+1, stop-1]
