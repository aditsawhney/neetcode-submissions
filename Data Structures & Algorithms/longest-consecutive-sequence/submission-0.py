class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        max_streak = 0

        for number in number_set:
            if (number-1) not in number_set:
                # ensure that the no previously consecutive number exists
                current_number = number     
                current_streak = 1

                while (current_number + 1) in number_set:
                    current_number += 1
                    current_streak += 1

                max_streak = max(max_streak, current_streak)
        return max_streak