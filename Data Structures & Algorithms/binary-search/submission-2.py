class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minv = 0
        maxv = len(nums)-1
        mid = (minv+maxv)//2
        while minv<=maxv:
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr > target:
                maxv = mid-1
            else:
                minv = mid+1
            mid = (minv+maxv)//2
        return -1
