class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        checked = []
        for index, char in enumerate(s):
            if char not in checked:
                if char not in s[index+1:]:
                    return index
                else:
                    checked.append(char)
        return -1
