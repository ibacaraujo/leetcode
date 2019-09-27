class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      print(nums1)
      print(nums2)
      # first thing, to merge the arrays
      def merge(arr1, arr2):
        i1 = 0
        i2 = 0
        new_array = []
        if len(arr1) == 0:
          new_array = arr2
          return new_array
        if len(arr2) == 0:
          new_array = arr1
          return new_array
        for i in range(len(arr1) + len(arr2)):
          if arr1[i1] <= arr2[i2]:
            new_array.append(arr1[i1])
            i1 += 1
          else:
            new_array.append(arr2[i2])
            i2 += 1
          if i1 == len(arr1):
            new_array.extend(arr2[i2:])
            break
          if i2 == len(arr2):
            new_array.extend(arr1[i1:])
            break
        return new_array
      nums = merge(nums1, nums2)
      print(nums)
      # then calculate the median
      if len(nums) % 2 == 0:
        return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
      else:
        return nums[len(nums) // 2]
