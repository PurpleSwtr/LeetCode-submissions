class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)

        # for left, num in enumerate(nums1):
        #     if nums1[left] not in nums2:
        #         nums1.remove(nums1[left])

        # return res

