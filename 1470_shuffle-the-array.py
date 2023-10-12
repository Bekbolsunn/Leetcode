class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

q = Solution()
print(q.shuffle(nums = [2,5,1,3,4,7], n = 3))
