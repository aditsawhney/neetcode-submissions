class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = s.lower()
        res = ""
        for character in input:
            if 48 <= ord(character) <= 57 or 97 <= ord(character) <= 122:
                res += character
            
        return res == res[::-1]