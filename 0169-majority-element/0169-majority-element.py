class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}
        
        for i in nums:
            
            if i not in dic:
                
                dic[i] = 1
                
            else:
                
                dic[i] += 1
                
        
        max_val = 0
        majority_elem = 0
                
                
        for key, value in dic.items():
            
            if value > max_val:
                
                
                max_val = value
                majority_elem = key
                
                
        return majority_elem
            
            
        