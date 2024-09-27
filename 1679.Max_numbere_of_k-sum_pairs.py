def maxOperations(nums: list[int], k: int) -> int:
        re_dict = {}
        i = 0
        j = 1
        counter = 0
        while True: 
            
            print("len before break",len(nums))
            print("before break i=",i," j=",j)
            
            if(i == len(nums)-1 or len(nums)==0): break
            
            re_dict[nums[i]] = k-nums[i]
            print("dict",re_dict)
            print("i=",i," j=",j)
            if nums[j] == re_dict[nums[i]] :
                del re_dict[nums[i]]
                del nums[i]
                print("after i","i=",i," j=",j)
                del nums[j-1]
                counter += 1
                i=0
                j=1
            print("nums",nums)
            print("i=",i," j=",j)
            print("counter ",counter)
            print("len",len(nums))
            
        
            if(j >= len(nums)):
                i += 1
                j = i + 1 
            else:
                j += 1
            
            if(j>=len(nums)):
                j-= 1;
                
            
            print("-------------")
        return counter
    
print("final counter",maxOperations(nums=[1,2,3,4],k =5))