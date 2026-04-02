class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr = nums[0] ^ nums[1]
        
        for i in range(2,len(nums)):
            curr ^= nums[i]
        return curr