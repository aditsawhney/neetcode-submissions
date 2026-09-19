class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        alt_till = min(m, n)

        final = ""
        for i in range(alt_till):
            final += word1[i]
            final += word2[i]
        
        if m > alt_till:
            final += word1[alt_till:]
        elif n > alt_till:
            final += word2[alt_till:]
        
        return final
