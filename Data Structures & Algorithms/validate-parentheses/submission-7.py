class Solution:
    def isValid(self, s: str) -> bool:
        left = {"(", "{", "["}
        right = {")", "}", "]"}
        match = {"(": ")", "{": "}", "[": "]"}
        stack = []
        if s[0] in right: return False
        if len(s)%2==1: return False
        for char in s:
            if char in left:
                stack.append(char)
            if char in right:
                if stack and char != match[stack.pop()]:
                    return False
        if stack: return False
        return True


        
        