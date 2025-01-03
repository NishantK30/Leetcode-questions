'''##### Description -
Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

##### Example -
**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1
**Output:** [1]

##### Logic -
Logic 1: Use a  counter and heap
->we count the frequency of each element and store in a dictionary.
->create a heap from tuple (-value,key) 
->we use - value since normally heapq will create a min heap and adding negative sign makes it pseudo max heap

Logic 2: Use a counter and heap with n largest element
-> we can create a heap with keeps track of only the n largest elements

Logic 3: there is another method using Quickselect which is a bit hard [[Check later]] '''

##### Python Solution -
#logic 1 solution -

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter ={}
        heap = []
        
        for i in nums:
         #counter[n]=1+counter.get(n,0) does same thing as the loop below
            if i in counter.keys():
                counter[i]+=1
            else:
                counter[i]=1

        for key,value in counter.items():
            heapq.heappush(heap,(-value,key))
        result = []

        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result

#logic 2 solution -

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]

'''Step 1: Count the frequency of each number in nums
Step 2: Use a heap to keep track of the k most frequent elements `heapq.nlargest` will return the k largest elements based on frequency. We are using a tuple (frequency, number) so we can compare by frequency. `heapq.nlargest` is efficient because it only needs to track the k largest values.
We are pushing the (-freq, num) because heapq is a min-heap by default.
By using negative frequency, we are turning it into a max-heap behavior.
##### 1. **`heapq.nlargest(k, iterable, key=...)`**

- **Functionality**: This function retrieves the top `k` largest elements from an iterable based on a specified key.
- **Parameters**:
    - `k`: The number of largest elements to return.
    - `iterable`: The collection to extract elements from. In this case, `freq.items()`.
    - `key`: A function that specifies how to sort or compare the elements. Here, it's `lambda x: x[1]`, which means the second value of each tuple (the dictionary value) is used as the sorting key.'''
