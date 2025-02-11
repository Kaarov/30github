class Solution:
    def constructRectangle(self, area):
        ans = int(area ** 0.5)
        for l in range(ans, 0, -1):
            if area % l == 0:
                return [area // l, l]


if __name__ == "__main__":
    slt = Solution()
    print(slt.constructRectangle(4))  # [2, 2]
    print(slt.constructRectangle(37))  # [37, 1]
    print(slt.constructRectangle(122122))  # [427, 286]
