class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # res = []
        res = set()
        temp = []
        sorted_nums = sorted(nums)

        for pos, num in enumerate(sorted_nums):

            sorted_arr = sorted_nums[:]
            sorted_arr.pop(pos)

            i = 0
            j = len(sorted_arr)-1

            while i < j:

                if sorted_arr[j] + sorted_arr[i] > -num:
                    j -= 1

                elif sorted_arr[j] + sorted_arr[i] < -num:
                    i += 1

                else:
                    
                    if num >= sorted_arr[j]:

                        # temp = [sorted_arr[i], sorted_arr[j], num]
                        temp = (sorted_arr[i], sorted_arr[j], num)

                    elif num <= sorted_arr[i]:

                        temp = (num, sorted_arr[i], sorted_arr[j])
                        # temp = [sorted_arr[i], sorted_arr[j], num]

                    else:

                        temp = (sorted_arr[i], num, sorted_arr[j])
                        # temp = [sorted_arr[i], sorted_arr[j], num]
                        
                        
                    res.add(temp)
               

                    # if temp not in res:

#                         res.append(temp)
                        
                    i += 1
                    j -= 1
                    
                    
                    temp = []
                    
                    
        return res
        
