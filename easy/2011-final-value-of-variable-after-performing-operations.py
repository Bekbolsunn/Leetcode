class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        count = 0
        for i in operations:
            if i == "--X" or i == "X--":
                count -= 1
            elif i == "++X" or i == "X++":
                count += 1
        return count


q = Solution()
print(q.finalValueAfterOperations(operations=["++X", "++X", "X++"]))
