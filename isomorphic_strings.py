class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False   
        for i in range(len(s)):
            if s[i] in d:
                continue
            else:
                d[s[i]] = t[i]
        for i in range(len(t)):
            if d[s[i]] != t[i]:
                return False    
        return True
        
