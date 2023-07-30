class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for arr in matrix:
            
            
        
            
        
            if target >= arr[0] and target <= arr[-1]:

                left = 0
                right = len(arr) - 1
                

                while left <= right:

                    mid = (left + right) // 2

                    if arr[mid] == target:
                        return True

                    elif target < arr[mid]:
                        right = mid - 1

                    else:
                        left = mid + 1

        return False
        
        
        
        