class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = [
            char for char in s.lower()
            if char in 'abcdefghijklmnopqrstuvwxyz01234567890'
        ]

        left = 0
        right = len(letters) - 1
        while left < right:
            if letters[left] != letters[right]:
                return False
            left += 1
            right -= 1
        return True
