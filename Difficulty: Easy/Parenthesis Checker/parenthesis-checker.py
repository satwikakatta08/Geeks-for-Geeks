class Solution:
    def isBalanced(self, s):
        # code here
        par={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in par:
                top=stack.pop() if stack else '#'
                if par[char]!=top:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
            
        