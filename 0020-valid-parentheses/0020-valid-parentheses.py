class Solution:
    def isValid(self, s: str) -> bool:
        
        ref = {"(":")", "{":"}", "[":"]"}
        stack = []
        
        for i in s:
            
            if i in ref:
                stack.append(i)
                
            elif len(stack) == 0 or ref[stack.pop()] != i:
                return False
            
        return len(stack) == 0
                
                
        