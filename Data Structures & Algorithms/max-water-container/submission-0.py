class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i = 0
        j = len(heights)-1
        while i<j:
            size = min(heights[i],heights[j])*abs(j-i)
            print(size)
            biggest = max(biggest,size)
            if heights[i]>=heights[j]: j-=1
            else: i+=1
        return biggest

