class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret = []
        count = 0
        j = 0
        for i in range(len(s)):
            if s[i] == '(':
                count +=1
            elif s[i] == ')':
                count -=1
            if count == 0:
                ret.append([j+1, i])
                j = i + 1
        return  "".join(ret)









        pass