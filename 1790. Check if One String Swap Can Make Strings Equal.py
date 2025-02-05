from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2): return False
        if s1 == s2: return True

        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

        return count < 3


if __name__ == "__main__":
    slt = Solution()
    print(slt.areAlmostEqual(s1="bank", s2="kanb"))  # True
    print(slt.areAlmostEqual(s1="attack", s2="defend"))  # False
    print(slt.areAlmostEqual(s1="kelb", s2="kelb"))  # True

# Done ✅
