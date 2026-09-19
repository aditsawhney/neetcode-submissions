class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, element in enumerate(nums):
            required = target - element

            if required in seen:
                return [seen[required], index]

            seen[element] = index
        
        return []