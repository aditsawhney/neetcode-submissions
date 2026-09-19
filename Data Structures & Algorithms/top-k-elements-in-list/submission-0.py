class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        freq_list = []
        for key, value in freq.items():
            freq_list.append([key, value])
        
        freq_list.sort(key=lambda x:x[1], reverse = True)
        freq_number_list = freq_list[:k]
        ans = []

        for pair in freq_number_list:
            ans.append(pair[0])
        
        return ans