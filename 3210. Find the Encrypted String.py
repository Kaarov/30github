class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        idx = k % len(s)
        return s[idx:] + s[:idx]
