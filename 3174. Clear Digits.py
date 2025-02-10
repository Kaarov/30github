class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    slt = Solution()
    print(slt.clearDigits("abc"))  # "abc"
    print(slt.clearDigits("cb34"))  # ""
