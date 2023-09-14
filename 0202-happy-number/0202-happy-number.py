class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        
        data = []

        def checkHappy(n, data):

            nums = [int(i) for i in str(n)]

            res = 0


            for num in nums:

                res += (num*num)





            if res not in data:
                data.append(res)

            else:
                return False

            if res == 1:

                return True


            else:

                return checkHappy(res, data)


        return checkHappy(n, data)