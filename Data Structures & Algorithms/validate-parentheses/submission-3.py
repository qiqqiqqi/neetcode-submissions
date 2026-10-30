class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        for i in s:
            if i == '(':
                ans.append(')')
            elif i == '{':
                ans.append('}')
            elif i == '[':
                ans.append(']')
            else:
                if len(ans)==0 or ans.pop(-1)!=i :
                    return False
        if(len(ans)==0):
            return True
        else:
            return False
