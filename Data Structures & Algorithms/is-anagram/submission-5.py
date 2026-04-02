class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s_set = {}
        for char in s:
            if char in s_set:
                s_set[char]+=1
            else:
                s_set[char]=1
        for char in t:
            if char not in s_set:
                return False
            s_set[char]-=1
            if s_set[char]<0:
                return False
        return True