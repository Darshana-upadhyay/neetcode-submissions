class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        for num in nums:
            if num != 0:
                prod = prod * num
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return [0] * len(nums) 

        res = []

        for num in nums:
            if zero_cnt:
                res.append(0) if num != 0 else res.append(prod)
                continue
            res.append(prod//num)

        return res



