class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        for i in range(len(command)):
            if command[i] == 'G':
                result += 'G'
            elif command[i] == "a":
                result += 'al'
            elif command[i] == "(" and command[i + 1] == ")":
                
                result += 'o'
        # return result
        print(command[i], i)
    
q = Solution()
print(q.interpret(command = "G()(al)")) #"Goal"
print(q.interpret(command = "G()()()()(al)")) #"Gooooal"
print(q.interpret(command = "(al)G(al)()()G")) #"alGalooG"