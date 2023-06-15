class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flower_counter = 0
        
        for index, flower in enumerate(flowerbed):
            if flowerbed[index] == 0 and (index == 0 or flowerbed[index-1] == 0 ) and (index ==               len(flowerbed)-1 or flowerbed[index+1] == 0):
                flowerbed[index] = 1
                flower_counter += 1
            
        if flower_counter >= n:
            return True
        else:
            return False
            
            

        
        
            
        
       
        
        
        