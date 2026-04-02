class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            num1 = num
            length = 0
            while num1 in num_set:
                length += 1
                num1 += 1
            longest=max(longest,length)
        return longest
                
