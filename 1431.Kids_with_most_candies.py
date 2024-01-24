'''There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.'''

candies = [2,3,5,1,3]
extraCandies = 3

max_num = max(candies)
print(max_num)
result=[]
for i in range(len(candies)):
    new_max_num = candies[i] +  extraCandies
    print('new',new_max_num)
    if new_max_num > max_num:
        result.append(True)
    else:
        result.append(False)
    new_max_num = 0
      
print(result)