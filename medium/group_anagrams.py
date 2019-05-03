class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            word = ''.join(sorted(s))
            if word not in d:
                d[word] = [str(s)]
            else:
                d[word].append(str(s))
        return d.values()
