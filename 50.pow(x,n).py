class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def calc(num = x, exp = abs(n)):
            print(num)
            print('exp :-',exp)
            if exp == 0:
                return 1
            elif exp % 2 == 0:
                return calc(num*num , exp//2)
            else:
                return num * calc(num*num, (exp-1)//2)
        
        result = calc()
        if n > 0 : 
            return result
        else:
            return  1/result
        
d = Solution()
d.myPow(2,6)