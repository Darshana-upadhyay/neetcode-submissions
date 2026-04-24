class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            k = i + 1
            for k in range(len(numbers)):
                if numbers[i] + numbers[k] == target:
                    return [i+1, k+1]
        return []
