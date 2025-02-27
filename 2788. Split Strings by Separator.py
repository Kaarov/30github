from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            word = word.split(separator)
            ans.extend([w for w in word if w is not ""])
        return ans
