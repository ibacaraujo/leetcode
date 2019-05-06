class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        #result = str(float(numerator)/denominator)
        if not denominator:
            return
        if not numerator:
            return '0'
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        result.append(str(numerator//denominator))
        remainder = numerator % denominator
        if not remainder:
            return "".join(result)
        result.append(".")
        d = dict()
        while remainder:
            if remainder in d:
                result.insert(d[remainder], "(")
                result.append(")")
                break
            d[remainder] = len(result)
            quotient, remainder = divmod(remainder*10, denominator)
            result.append(str(quotient))
        return "".join(result)
