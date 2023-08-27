class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        sortedNums = sorted(nums)
        
        for i in range(len(nums)):
            source = sortedNums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                potentialSum = source + sortedNums[j] + sortedNums[k]
                if potentialSum > 0:
                    k -= 1
                elif potentialSum < 0:
                    j += 1
                else:
                    if [source, sortedNums[j], sortedNums[k]] not in ans:
                        ans.append([source, sortedNums[j], sortedNums[k]])
                    k -= 1
                    j += 1
        return ans