'''You are given a positive integer num. 
You may swap any two digits of num that have the same parity 
(i.e. both odd digits or both even digits).
Return the largest possible value of num after any number of swaps.

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 
3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 
is the largest possible number.'''
import heapq
#sol 1
class Solution:
    def largestInteger(self, num: int) -> int:
        even_heap = []
        odd_heap = []

        num_s = str(num)
        for char in num_s:
            digit = int(char)
            if digit % 2 == 0:
                heapq.heappush(even_heap,-digit)
            else:
                heapq.heappush(odd_heap,-digit)
        
        res = []

        for char in num_s:
            if int(char) % 2 == 0:
                digit = - heapq.heappop(even_heap)
            else:
                digit = - heapq.heappop(odd_heap)
            res.append(str(digit))
        
        return int("".join(res))
    
#sol 2
class Solution:
    def largestInteger(self, num: int):
        n = len(str(num))
        arr = [int(i) for i in str(num)]
        odd, even = [], []
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        odd.sort()
        even.sort()
        res = 0
        for i in range(n):
            if arr[i] % 2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res

#cpp sol
'''
class Solution {
public:
    int largestInteger(int num) {
        priority_queue <int> even_heap, odd_heap;
        string num_s = to_string(num);

        for(const char& ch: num_s){
            int c_num = ch;
            if (c_num%2 == 0){
                even_heap.push(c_num);
            }else{
                odd_heap.push(c_num);
            }
        }
        
        int evenidx = 0, oddidx = 0, n = num_s.size();
        for(int i = 0; i<n; i ++){
            if(num_s[i]%2==0){
                num_s[i] = even_heap.top();
                even_heap.pop();
            } else{
                num_s[i] = odd_heap.top();
                odd_heap.pop();
            }   
        }
        return stoi(num_s);

    }
};
'''