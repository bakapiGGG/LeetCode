class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        from math import factorial
        
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
        