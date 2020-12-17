class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest_wealth = 0
        for account in accounts:
            richest_wealth = max(richest_wealth, sum(account))
        return richest_wealth
