class Solution:
    def isValid(self, s: str) -> bool:
        
        # ([{((()))}])
        # ([[]){}({})[()]
        
        stack = []
#         stack is going to keep track of the order of open brackets
        dictionary = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        
        for char in s:
            if char in dictionary:
# most efficient way is to check the case that is invalid
# make sure the char we're looking at maps to an opening bracket, which should be the most recently added to the stack 
                if len(stack) == 0:
                    return False
                if stack[-1] != dictionary[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
#       this evaluates to return true or return false:
        return len(stack) == 0
    
# (((((())))) --> case where extra opening bracket