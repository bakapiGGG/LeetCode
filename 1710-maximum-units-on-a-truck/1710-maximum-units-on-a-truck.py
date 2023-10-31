class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        res = [[boxType, boxType[1]] for boxType in boxTypes]

        def takeSecond(elem):
            return elem[1]

        res.sort(key=takeSecond ,reverse=True)

        total = 0


        for i in res:

            truckSize = truckSize - i[0][0]

            if truckSize <= 0:
                truckSize += i[0][0]
                print(truckSize)

                while truckSize > 0:

                    truckSize = truckSize - 1
                    total += i[0][1]

                break

            else:
                total = total + i[0][0] * i[0][1]
                
                
        return total
        
        
        