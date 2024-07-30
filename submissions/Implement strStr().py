class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # for index in range(len(haystack)-len(needle)):
        #    if haystack[index:].startswith(needle):
        #        return index
        # return -1

        return haystack.find(needle)
