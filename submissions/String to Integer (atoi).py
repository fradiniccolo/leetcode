class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        # clean-up left side
        s = s.strip()
        negative = False
        for index, char in enumerate(s):
            if char in '0123456789':
                if index > 1 or s[0] not in '+-0123456789':
                    return 0
                elif s[0] == '-':
                    negative = True
                s = s[index:]
                break

        # clean-up right side
        num = []
        for char in s:
            if char in '0123456789':
                num.append(char)
            else:
                break
        if not num:
            return 0

        # to signed int
        num = int(''.join(num))
        if negative:
            num = -num

        # limit to boundary
        if num < -(2**31):
            num = -(2**31)
        elif num > (2**31)-1:
            num = 2**31-1

        return num
