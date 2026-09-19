class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     res = ""
    #     for s in strs:
    #         res += str(len(s)) + "#" + s
    #     return res

    # def decode(self, s: str) -> List[str]:
    #     res = []
        
    #     i = 0       # i is indicating as to where we are in our string
    #     while i < len(s):
    #         j = i
    #         while s[j] != "#":
    #             j += 1
    #         length = int(s[i:j])
    #         res.append(s[j+1:j+1+length])

    #         i = j+1+length
        
    #     return res

    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s:str) -> list[str]:
        result = []

        i = 0           # i is used to find position where we at in the string
        while i < len(s):
            j = i       # j is used to find the "#" symbol, which would indicate the beginning of the actual string

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            
            i = j+1+length
        return result
    