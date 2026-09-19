class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listForT = list(t)

        if len(s) != len(t):
            return False
        
        for character in s:
            if character in listForT:
                listForT.remove(character)
            else:
                return False
    
        return len(listForT) == 0 