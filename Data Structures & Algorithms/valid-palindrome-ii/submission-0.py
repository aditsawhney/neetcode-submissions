class Solution:
    def isPalindrome(self, input:str, left:int, right:int) -> bool:
        while left < right:
            if input[left] != input[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
            left += 1
            right -= 1
        
        return True