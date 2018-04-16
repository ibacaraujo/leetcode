class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        s_set = set()
        res = i = j = 0
        while i < n and j < n:
            if s[j] not in s_set:
                s_set.add(s[j])
                j = j + 1
                res = max(res, j - i)
            else:
                s_set.remove(s[i])
                i = i + 1
        return res