class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        i = 0
        j = len(nums) - 1
        c = 0
        
        arr = sorted(nums)
        
        while i < j:
    
            if arr[i] + arr[j] < k:
                i+= 1

            elif arr[i] + arr[j] > k:

                j-= 1

            else:
                arr.pop(0)
                arr.pop() 
                c+= 1
                j-=2
                
        return c
        