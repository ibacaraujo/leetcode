class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while n != 1:
            str_n = str(n)
            str_numbers = list(str_n)
            numbers = map(int, str_numbers)
            squares = [x**2 for x in numbers]
            n = sum(squares)
            if i > 1000:
                return False
            i += 1
        return True
