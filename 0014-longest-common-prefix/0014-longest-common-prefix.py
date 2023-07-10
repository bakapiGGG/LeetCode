class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i = strs[0]
        
        for word in strs:
            
            while word.startswith(i) is False:
                
                i = i[:-1]
                
        return i
        