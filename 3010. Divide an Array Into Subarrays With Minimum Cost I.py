from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums.pop(0)
        nums.sort()
        return first + nums.pop(0) + nums.pop(0)
