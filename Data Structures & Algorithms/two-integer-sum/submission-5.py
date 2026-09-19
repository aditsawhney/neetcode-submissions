class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            element = nums[i]
            remaining = target - element
            if remaining in hash_map:
                return [hash_map[remaining], i]
            else:
                hash_map[nums[i]] = i