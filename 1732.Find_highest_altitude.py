# There is a biker going on a road trip. 
# The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n 
# where gain[i] is the net gain in altitude between points i​​​​ and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

#PYTHON
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new_gain = 0
        altitudes = []
        altitudes.append(new_gain)
        for i in gain:
            new_gain += i
            altitudes.append(new_gain)
        
        return max(altitudes)
    
#CPP 1
# class Solution {
# public:
#     int largestAltitude(vector<int>& gain) {
#         int new_gain = 0;
#         vector<int>altitudes;
#         altitudes.push_back(new_gain);
#         for(const int& i : gain){
#             new_gain += i;
#             altitudes.push_back(new_gain);
#         }

#         return *max_element(altitudes.begin(),altitudes.end());

#     }
# };

# CPP 2
# class Solution {
# public:
#     int largestAltitude(vector<int>& gain) {
#         int n=gain.size();
#         int m=gain[0];;
#         for(int i=1;i<n;i++){
#             gain[0]=gain[i]+gain[0];
#             m=max(m,gain[0]);
#         }
#         if(m<0){
#             return 0;
#         }
#         return m;
#     }
# };