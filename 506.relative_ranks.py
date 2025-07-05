'''You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.


Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].'''
import heapq
#sol 1
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        tup = []
        for ind, val in enumerate(score):
            tup.append((-val,ind))
        
        heapq.heapify(tup)
        answer = [''] * len(score)
        i = 0
        while tup:
            ind = heapq.heappop(tup)[1]
            if i >= 3:
                answer[ind] = f'{i+1}'
            elif i == 0:
                answer[ind] = "Gold Medal"
            elif i == 1:
                answer[ind] = "Silver Medal"
            elif i == 2:
                answer[ind] = "Bronze Medal"
            i+=1
        
        return answer
    
#sol 2
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_scores = sorted(score, reverse = True)
        ranks = {sorted_scores[i]: str(i+1) for i in range(len(score))}
        ranks[sorted_scores[0]] = "Gold Medal"
        if len(score) > 1:
            ranks[sorted_scores[1]] = "Silver Medal"
        if len(score) > 2:
            ranks[sorted_scores[2]] = "Bronze Medal"
        
        return [ranks[s] for s in score]
    
#cpp sol 1
"""class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> sorted_scores = score;
        sort(sorted_scores.begin(),sorted_scores.end(), greater<int>());
        unordered_map<int,string> rank;
        vector<string> medal = {"Gold Medal","Silver Medal","Bronze Medal"};
        for(int i= 0;i<score.size();i++){
            if( i < 3){
                rank[sorted_scores[i]] = medal[i];
            }
            else{
                rank[sorted_scores[i]] = to_string(i+1);
            }
            
        }

        vector<string> answer;
        for(const int& j: score){
            answer.push_back(rank[j]);
        }

        return answer;

    }
};"""

#cpp sol 2
'''class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        priority_queue<pair<int, int>> pq;

        int n = score.size();

        for (int i = 0; i < n; i++)
            pq.push({score[i], i});

        vector<string> ans(n);
        int i = 1;

        while (!pq.empty()) {
            auto [s, idx] = pq.top();
            pq.pop();

            if (i > 3)
                ans[idx] = to_string(i);
            else if (i == 1)
                ans[idx] = "Gold Medal";
            else if (i == 2)
                ans[idx] = "Silver Medal";
            else if (i == 3)
                ans[idx] = "Bronze Medal";

            i++;
        }
        return ans;
    }
};'''