class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        for i in range(1, numRows+1):

            if i == 1:

                res.append([1])

            elif i == 2:

                res.append([1, 1])

            elif i == 3:

                res.append([1, 2, 1])

            else:
                temp = [1]
                prev_arr = i-2

                for j in range(1,  i-1):


                    temp.append(res[prev_arr][j] + res[prev_arr][j-1])

                temp.append(1)

                res.append(temp)
                
        return res
        