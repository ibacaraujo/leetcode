#4 Median of Two Sorted Arrays

def findMedianSortedArrays(nums1, nums2):
	m = len(nums1)
	n = len(nums2)
	nums = []
	i = 0, j = 0
	while i < m or j < n:
		if nums1[i] <= nums2[j]:
			nums.append(nums1[i])
			i = i + 1
		else:
			nums.append(nums2[j])
			j = j + 1
	if len(nums) % 2 == 0:
		return float((nums[len(nums)/2 - 1] + nums[len(nums/2)])/2)
	else:
		return nums[len(nums)/2]