class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequences_counter = dict()
        for i in range(len(s)+1-10):
            if s[i:i+10] in sequences_counter:
                sequences_counter[s[i:i+10]] += 1
            else:
                sequences_counter[s[i:i+10]] = 1
        return [key for key, value in sequences_counter.items() if value > 1]
    
