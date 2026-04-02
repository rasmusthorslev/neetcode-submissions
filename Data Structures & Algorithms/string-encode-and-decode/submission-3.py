class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded+=f"{len(string)}#{string}"
        return encoded


    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            strings.append(s[j+1:j+1+length])
            i = j + 1 + length
        return strings
            