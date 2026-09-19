class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listForT = list(t)
        
        for character in s:
            if character in listForT:
                listForT.remove(character)
            else:
                return False
    
        return len(listForT) == 0 