from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        numbers = defaultdict(list)
        for i in range(len(nums)):
            number = 0
            for digit in str(nums[i]):
                number += int(digit)
            numbers[number].append(nums[i])
        ans = 0
        count = 0
        for number in numbers.values():
            if len(number) <= 1:
                count += 1
            else:
                max_num = max(number)
                number.remove(max_num)
                max_num += max(number)
                ans = max(ans, max_num)
        if count == len(numbers):
            return -1
        return ans
