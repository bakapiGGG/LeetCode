class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        stack = []
        for num in nums:
            for subset in ans:
                new_subset = subset + [num]
                stack.append(new_subset)
            ans += stack
            stack = []
        return ans