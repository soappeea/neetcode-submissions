class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
            
        stack = []
        closeToOpen = {']':'[', ')':'(', '}':'{'} # for checking if closing has opening in stack
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        if not stack:
            return True
        
        return False