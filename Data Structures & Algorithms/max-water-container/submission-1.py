class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        k = len(heights)-1
        max_water = 0
        while j<k:
            water = (k-j)*min(heights[j],heights[k])
            max_water = max(max_water, water)
            if heights[j]<heights[k]:
                j+=1
            else:
                k-=1
        return max_water