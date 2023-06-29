class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        subarr_sum = sum(nums[:k])
        res = [subarr_sum]
        
        for i in range(len(nums)-k):
            
            subarr_sum -= nums[i]
            subarr_sum += nums[i+k]
            
            res.append(subarr_sum)
            
        return max(res)/k
        
        
#         max_avg = -10000
#         c = 0
        
#         for i in range(len(nums)//k + 1):
              
#             avg = sum(nums[c:c+k])/k
#             if avg >= max_avg:
#                 max_avg = avg
                
#             c+=1
                
                
#         return max_avg


        