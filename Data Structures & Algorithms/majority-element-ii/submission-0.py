class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        majority_list = []
        for key, value in freq.items():
            if value > (len(nums)/3):
                majority_list.append(key)
        
        return majority_list