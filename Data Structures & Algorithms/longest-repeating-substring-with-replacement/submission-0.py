class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_length = 0
        character_set = set(s)

        # check for each element of the string as the target element
        for target in character_set:
            start = 0
            skipped_count = 0

            for end in range(len(s)):
                # if element not in character set, replacement required
                if s[end] != target:
                    skipped_count += 1
                
                # if replacements > k, shrink window size
                while skipped_count > k:
                    if s[start] != target:
                        skipped_count -= 1
                    start += 1
                
                # update max length
                current_length = end - start + 1
                max_length = max(max_length, current_length)
        
        return max_length
