class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftmax = [0] * len(height)
        for i in range(1, len(height)):
            leftmax[i] = max(height[i-1],leftmax[i-1])
        rmax = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            rmax[i] = max(height[i+1],rmax[i+1])
        for i in range(1,len(height)-1):
            water = min(leftmax[i],rmax[i])-height[i]
            if water > 0:
                res += water

        return res 