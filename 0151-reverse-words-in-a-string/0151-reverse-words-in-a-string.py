class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        words = list()
        
        for word in s.split(" "):
            words.append(word)
            
        words.reverse()
        
        words = [word for word in words if word != ""]
        
        final = " ".join(words)
        
        return final
        