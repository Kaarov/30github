from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_count = defaultdict(int)
        ball_to_color = defaultdict(int)

        ans = []

        for ball, color in queries:
            if ball in ball_to_color:
                color_count[ball_to_color[ball]] -= 1

                if color_count[ball_to_color[ball]] == 0:
                    del color_count[ball_to_color[ball]]

            ball_to_color[ball] = color
            color_count[color] += 1

            ans.append(len(color_count.keys()))

        return ans


if __name__ == "__main__":
    slt = Solution()
    print(slt.queryResults(
        limit=4,
        queries=[[1, 4], [2, 5], [1, 3], [3, 4]],
    ))  # [1, 2, 2, 3]
    print(slt.queryResults(
        limit=4,
        queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]],
    ))  # [1, 2, 2, 3, 4]
