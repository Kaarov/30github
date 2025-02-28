class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        count = 0
        while True:
            ans = 3 ** count
            if ans == n:
                return True
            if ans > n:
                return False
            count += 1
