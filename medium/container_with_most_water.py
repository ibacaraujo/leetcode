class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        if j == 1:
            return 1*min(height[i], height[j])
        max_area = -1
        while i < j:
            area = (j-i)*min(height[i], height[j])
            if max_area < area:
                max_area = area
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area
