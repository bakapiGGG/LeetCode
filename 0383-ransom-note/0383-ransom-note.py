class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_dict = {}
        ransomNote_dict = {}
        
        for char in magazine:
            
            if char in magazine_dict:
                
                magazine_dict[char] += 1
                
            else:
                
                magazine_dict[char] = 1
                
        for char in ransomNote:
        
            if char in ransomNote_dict:
                
                ransomNote_dict[char] += 1
                
            else:
                
                ransomNote_dict[char] = 1
                
        print("magazine:", magazine_dict)
        print("ransom:", ransomNote_dict)
                
        for key in ransomNote_dict:
            
            if key not in magazine_dict or ransomNote_dict[key] > magazine_dict[key]:
                
                return False
                
      
            
        return True
                
                
        
       
        