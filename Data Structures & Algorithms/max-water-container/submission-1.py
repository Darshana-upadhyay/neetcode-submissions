class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        r = len(heights) - 1
        l = 0
        while(l<r):
            h = min(heights[l],heights[r])
            b = r - l
            if maxarea < (h * b):
                maxarea = h * b
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea
        