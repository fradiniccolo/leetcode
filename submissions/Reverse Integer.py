class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = list(str(abs(x)))
        x.reverse()
        x = ''.join(x)
        x = int(x)
        if negative:
            x = -x
        if not -(2**31) <= x <= 2**31 - 1:
            return 0
        return x
