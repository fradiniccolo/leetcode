class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        def counter(string):
            count = {}
            for char in string:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] += 1
            return count

        return counter(s) == counter(t)
