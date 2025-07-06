'''Given an array of points where points[i] = [xi, yi] 
represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order.
The answer is guaranteed to be unique (except for the order that it is in)

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''
import heapq
#sol 1
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = [] 

        for i in range(len(points)):
            dist = -self.distance(points[i])
            if len(min_heap) < k :
                heapq.heappush(min_heap,[dist,i])
            else:
                if dist > min_heap[0][0]:
                    heapq.heappushpop(min_heap,[dist,i])

        res = [points[i] for dist,i in min_heap ]

        return res
    
#cpp sol
'''
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int,vector<int>>> max_heap;

        for (auto point:points){
            int x = point[0];
            int y = point[1];
            int dist = x*x + y*y;
            if(max_heap.size()<k){
                max_heap.push({dist,point});
            }else{
                if(dist < max_heap.top().first){
                    max_heap.pop();
                    max_heap.push({dist,point});
                }
            }
        }

        vector<vector<int>> res;
        while(max_heap.size()>0){
            vector<int> entry = max_heap.top().second;
            res.push_back(entry);
            max_heap.pop();
        }

        return res;

    }
};
'''

