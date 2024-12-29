def productExceptSelf(nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        rightProd=1
        
        for i in range(1,n):
            result[i] = result[i-1]*nums[i-1]
        
        for i in range(n-1,-1,-1):
            result[i] *= rightProd
            rightProd *= nums[i]
        
        
        print(result)
            
        
productExceptSelf([1,2,3,4])