class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        stringified_strs_list = ""
        str_lengths = ""
        for string in strs:
            stringified_strs_list+=str(string)
            str_lengths+=str(len(string))+","
        return str_lengths+"#"+stringified_strs_list

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        curr_length = 0
        str_lengths, stringified_strs_list = s.split("#",1)
        str_lengths = str_lengths.split(",")
        for str_length in str_lengths:
            if str_length == "": continue
            str_length = int(str_length)
            word = stringified_strs_list[curr_length:curr_length+str_length]
            decoded.append(word)
            curr_length+=str_length
        return decoded

