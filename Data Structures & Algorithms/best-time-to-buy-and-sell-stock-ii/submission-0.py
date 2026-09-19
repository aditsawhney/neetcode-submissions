class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        for i in range(len(nums)-1):
            current_price = nums[i]
            next_price = nums[i+1]
            if next_price > current_price:
                profit += (next_price - current_price)

        return profit