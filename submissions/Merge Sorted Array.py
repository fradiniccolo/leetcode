class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            for index, num2 in enumerate(nums2):
                nums1[index+m] = num2
            if m+n > 1:
                nums1_needed_sorting = True
                while nums1_needed_sorting:
                    nums1_needed_sorting = False
                    for index in range(len(nums1[:-1])):
                        if nums1[index] > nums1[index+1]:
                            _ = nums1[index]
                            nums1[index] = nums1[index+1]
                            nums1[index+1] = _
                            nums1_needed_sorting = True
