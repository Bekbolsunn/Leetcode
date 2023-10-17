class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return sum(max(accounts, key=sum))
            
            
q = Solution()
print(q.maximumWealth(accounts=[[1,5],[7,3],[3,5]]))
