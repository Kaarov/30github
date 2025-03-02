from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = {}
        for idx, num in nums1:
            ans[idx] = ans.get(idx, 0) + num

        for idx, num in nums2:
            ans[idx] = ans.get(idx, 0) + num

        return sorted([[key, value] for key, value in ans.items()], key=lambda x: x[0])
