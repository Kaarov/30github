from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) > 1:
                ans.append(i)
        return ans
