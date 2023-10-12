class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        unique_elements = set(nums)
        result = []
        for i in unique_elements:
            count = 0
            for num in nums:
                if num == i:
                    count += 1
            result.append((i, count))

        count_unique = 0
        for _, count in result:
            count_unique += (count * (count - 1)) // 2

        return count_unique


q = Solution()
print(q.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
