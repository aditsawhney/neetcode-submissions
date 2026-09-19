class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_final = "".join(sorted(s))
        t_final = "".join(sorted(t))
        return s_final == t_final