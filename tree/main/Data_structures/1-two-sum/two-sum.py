class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in remaining:
                return [i, remaining[comp]]
            remaining[num] = i    
        