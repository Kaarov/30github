class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p1, p2 = p.split("*")

        if not p1:
            return p2 in s
        if not p2:
            return p1 in s

        pos = s.find(p1)
        if pos == -1:
            return False

        return p2 in s[pos + len(p1):]
