class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            for k in stones:
                print(k)
                if i == k:
                    count += 1
        return count


q = Solution()
# print(q.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(q.numJewelsInStones(jewels="ebd", stones="bbb"))
