class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        counter1 = {num: nums1.count(num) for num in set1}
        counter2 = {num: nums2.count(num) for num in set2}

        counter = {}
        for key in set1 & set2:
            counter[key] = min((counter1[key], counter2[key]))

        results = []
        for num, count in counter.items():
            for _ in range(count):
                results.append(num)
        return results
