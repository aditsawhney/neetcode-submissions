class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        number_set = set()
        for number in nums:
            if number > 0:
                number_set.add(number)
        
        for i in range(1, len(nums)+2):
            if i not in number_set:
                return i