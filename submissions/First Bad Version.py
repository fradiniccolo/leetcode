# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def split_versions(vers_range=None):
            from math import ceil
            """splits a list like (left_range, middle_element, right_range)"""
            if vers_range is not None and len(vers_range) > 0:
                mid = int(
                    ceil(vers_range.start+(vers_range.stop-1-vers_range.start)/2))
                left = range(vers_range.start, mid)
                if left.start > left.stop:
                    left = None
                right = range(mid+1, vers_range.stop+1)
                if right.start > right.stop:
                    right = None
                return (left, mid, right)
            else:
                return None

        def find_version(n):
            """reduces the version candidates range by removing a halve at each loop"""
            candidates = range(1, n+1)
            while len(candidates) > 1:
                left, middle, right = split_versions(candidates)
                if isBadVersion(middle):
                    if len(left) == 1:
                        if isBadVersion(left.start):
                            return left.start
                        else:
                            return middle
                    if right:
                        candidates = range(candidates.start, middle+1)
                else:
                    candidates = range(middle+1, candidates.stop)
            return candidates.start

        return find_version(n)
