class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]   # move slow by one step
            fast = nums[nums[fast]]     # move fast by 2 steps
            if slow == fast:
                break       # stop when they meet
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow     