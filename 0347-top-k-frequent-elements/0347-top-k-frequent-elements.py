class Solution:
    from collections import Counter
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return [i[0] for i in Counter(nums).most_common(k)]
        