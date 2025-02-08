class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""


if __name__ == "__main__":
    slt = Solution()
    print(slt.largestGoodInteger("6777133339"))  # "777"
    print(slt.largestGoodInteger("2300019"))  # "000"
    print(slt.largestGoodInteger("42352338"))  # ""
    print(slt.largestGoodInteger("101010"))  # ""
