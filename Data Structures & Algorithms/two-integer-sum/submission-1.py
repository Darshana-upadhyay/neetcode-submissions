class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            req = target - nums[i]
            for j in range(i+1, len(nums)):
                if req == nums[j]:
                    return [i,j]

