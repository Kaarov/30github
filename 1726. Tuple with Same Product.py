from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt = defaultdict(int)
        pair_cnt = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pair_cnt[product] += product_cnt[product]
                product_cnt[product] += 1

        res = 0
        for i in pair_cnt.values():
            res += i * 8

        return res


if __name__ == "__main__":
    slt = Solution()
    print(slt.tupleSameProduct([2, 3, 4, 6]))  # 8
    print(slt.tupleSameProduct([1, 2, 4, 5, 10]))  # 16
