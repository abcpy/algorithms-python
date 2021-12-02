"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""
class Solution:
    def isValid(self, s):
        stack = []
        dict = {']':'[', '}':'{', ')':'('}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
        return stack == []


        pass