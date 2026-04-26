class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(len(height)-1):
            if i == 0:
                continue
            water = min(max(height[:i]), max(height[i+1:])) - height[i]
            if water > 0:
                res += min(max(height[:i]), max(height[i+1:])) - height[i]
        return res

            
