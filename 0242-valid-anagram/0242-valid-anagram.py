class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        string_s = sorted(list(s))
        string_t = sorted(list(t))
        
        return string_s == string_t
        
       