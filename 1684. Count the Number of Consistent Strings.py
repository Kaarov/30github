from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)
        for word in words:
            if set(word) - allowed == set():
                ans += 1
        return ans
