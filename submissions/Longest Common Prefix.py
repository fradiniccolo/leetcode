class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_prefix = ''

        if any([word == "" for word in strs]):
            return common_prefix

        index = 0
        while True:
            try:
                letters = [word[index] for word in strs]
                if len(set(letters)) == 1:
                    common_prefix += letters[0]
                    index += 1
                else:
                    break
            except IndexError:
                break

        return common_prefix
