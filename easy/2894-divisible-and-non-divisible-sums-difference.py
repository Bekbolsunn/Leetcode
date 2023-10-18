class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1, n+1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        return num1 - num2


q = Solution()
print(q.differenceOfSums(n = 10, m = 3))
print(q.differenceOfSums(n = 5, m = 6))
print(q.differenceOfSums(n = 5, m = 1))