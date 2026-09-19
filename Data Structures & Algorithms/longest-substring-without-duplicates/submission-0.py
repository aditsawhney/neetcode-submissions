class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_set = set()
        start = 0
        max_length = 0

        for end in range(len(s)):
            while s[end] in character_set:
                character_set.remove(s[start])
                start += 1
            character_set.add(s[end])

            current_window = end - start + 1
            max_length = max(current_window, max_length)
        
        return max_length