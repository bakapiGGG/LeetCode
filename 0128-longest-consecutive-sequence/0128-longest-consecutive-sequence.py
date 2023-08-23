class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        uniqueNums = set(nums)
        maxLength = 1
        for num in nums:
            if num - 1 in uniqueNums:
                continue
            else:
                lengthofSequence = 1
                while num + lengthofSequence in uniqueNums:
                    lengthofSequence += 1
                maxLength = max(maxLength, lengthofSequence)
        return maxLength
                