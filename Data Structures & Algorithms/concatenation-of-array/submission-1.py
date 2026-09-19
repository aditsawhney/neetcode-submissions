class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)       #initialize a list of zeroes, with length 2n
        i = 0
        while i<n:
            ans[i] = nums[i]
            ans[i+n] = nums[i]
            i = i+1
        return ans
    
        
