class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        a = nums
        b = nums
        a = a + b
        return a


q = Solution()
print(q.getConcatenation(nums=[1, 2, 1]))
