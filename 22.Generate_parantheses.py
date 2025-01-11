'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]'''


def generateParenthesis( n: int) -> list[str]:
        stack=[]
        res=[]
        def backtrack(openP,closeP):
            if closeP == openP==n:
                res.append("".join(stack))
                return
            if openP<n:
                stack.append("(")
                backtrack(openP+1,closeP)
                stack.pop()
            
            if closeP<openP:
                stack.append(")")
                backtrack(openP, closeP+1)
                stack.pop()
                
        backtrack(0,0)
        return res

print(generateParenthesis(3))
    