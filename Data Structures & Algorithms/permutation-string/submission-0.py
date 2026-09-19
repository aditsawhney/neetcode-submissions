class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # store the elements of s1 in a frequency map
        freq_s1 = {}
        for letter in s1:
            if letter in freq_s1:
                freq_s1[letter] += 1
            else:
                freq_s1[letter] = 1
        
        # make a window map for s2
        window_s2 = {}

        start = 0
        for end in range(len(s2)):
            character = s2[end]
            if character in window_s2:
                window_s2[character] += 1
            else:
                window_s2[character] = 1
        
            # if window size exceeds len of s1, shrink
            if (end-start+1) > len(s1):
                left_character = s2[start]
                # remove left character from the window map
                window_s2[left_character] -= 1
                # if count of left character becomes 0, remove entirely
                if window_s2[left_character] == 0:
                    del window_s2[left_character]
                start += 1
            
            # check s1 and window of s2
            if len(s1) == (end-start+1) and window_s2 == freq_s1:
                return True
        
        return False
