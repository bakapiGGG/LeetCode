class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxDict = {}
        for idx, num in enumerate(nums):
            if num not in idxDict:
                idxDict[num] = idx
            else:
                if idx - idxDict[num] <= k:
                    return True
                else:
                    idxDict[num] = idx
        return False
        