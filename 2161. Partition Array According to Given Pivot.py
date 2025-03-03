from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        pivots = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                pivots.append(num)
            else:
                more.append(num)
        return less + pivots + more
