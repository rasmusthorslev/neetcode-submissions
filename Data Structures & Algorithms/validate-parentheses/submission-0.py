class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                if pairs[stack.pop()] != c:
                    return False

        return len(stack) == 0