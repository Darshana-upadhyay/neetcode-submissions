class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            l , r = i +1, len(numbers) -1
            while l <= r:
                mid = (r-l)//2 + l
                if tmp == numbers[mid]:
                    return [i+1, mid+1]
                elif numbers[mid] > tmp:
                    r = mid - 1
                else:
                    l = mid + 1
        return []

