'''
##### Question no - 20
###### Description -Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

##### Logic - 
- We use a hash map and map *every closing bracket with its equivalent opening bracket*. 
- Then we iterate through the string whenever we encounter a character that is not in the keys of our map i.e an opening bracket we append it to stack.
- If we encounter an closing bracket we check for 
    1. if stack is empty
    2. if the top most element of stack is a closing bracket
- if either is true then we return false , if not then we pop the top most element from the stack 
'''

#python solution
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

#cpp solution
"""
class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        map<char,char>map;
        map[')'] = '(';
        map['}'] = '{';
        map[']'] = '[';

        for(const auto &c: s){
            if(map.count(c)==0) stack.push(c);
            else{ 
                if( stack.empty()|| stack.top()!=map[c]){
                return false;
                }
            stack.pop();            
            }

         }
         return stack.empty();
    }
};
"""