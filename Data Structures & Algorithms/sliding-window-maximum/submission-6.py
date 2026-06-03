class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        l = 0
        window = list()
        res = []
        mn = 0
        for r in range(len(nums)):
            window.append(nums[r])
            mn = max(window)
            if r -l +1 == k:
                res.append(mn)
                window.pop(0)
                l += 1

            
        return res

        