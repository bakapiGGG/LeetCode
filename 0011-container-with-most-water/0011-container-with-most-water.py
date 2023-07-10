class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_val = 0
        i = 0
        j = len(height)-1

        while i < j:

            val = (j - i) * min(height[j], height[i]) 

            if val > max_val:

                max_val = val

            else:

                if height[i] > height[j]:

                    j-= 1

                else:

                    i+= 1
                    
                    
        return max_val
        