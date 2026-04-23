class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            j = len(heights) - 1
            while(j != i):
                length = min(heights[i], heights[j])
                breadth = j - i
                if maxarea < (length * breadth):
                    maxarea = length * breadth
                j -= 1
        return maxarea
        