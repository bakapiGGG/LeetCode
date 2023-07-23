class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         import math
        
#         res = len(nums) * [1]
        
#         for i in range(len(res)):
            
#             deep_copy = nums[::]
#             deep_copy.pop(i)
            
#             res[i] = math.prod(deep_copy)
            
#         return res

        rev = nums[::-1]

        n = len(nums)

        left = [0]*n
        right = [0]*n
        
        left[0] = 1
        right[0] = 1

        for i in range(1, n):

            if i == 1:
                left[i] = nums[0]

            else:
                left[i] = left[i-1] * nums[i-1]

        for i in range(1, n):

            if i == 1:
                right[i] = rev[0]

            else:
                right[i] = right[i-1] * rev[i-1]


        right = right[::-1]


        return [a * b for a, b in zip(left, right)]