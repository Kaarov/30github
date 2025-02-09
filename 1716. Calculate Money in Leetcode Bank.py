class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        initial = 0
        for i in range(n):
            if i % 7 == 0:
                initial += 1
            ans += initial + i % 7

        return ans


if __name__ == "__main__":
    slt = Solution()
    print(slt.totalMoney(4))  # 10
    print(slt.totalMoney(10))  # 37
    print(slt.totalMoney(20))  # 96
