class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        r = len(heights) - 1
        l = 0
        while l < r:
            breadth = r - l
            length = min(heights[l], heights[r])
            area = length * breadth
            maxarea = max(maxarea, area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return maxarea
        