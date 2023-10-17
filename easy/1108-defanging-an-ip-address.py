class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = '[.]'
        for i in address:
            if '.' in i:
                x = address.replace('.', a)
        return x        
    
q = Solution()
print(q.defangIPaddr(address="1.1.1.1"))
