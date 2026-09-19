class Solution:
    def sortString(self, str1: str) -> str:
        str1_list = list(str1)
        str1_list.sort()
        return "".join(str1_list)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for string in strs:
            key = self.sortString(string)
            if key not in hash_map:
                hash_map[key] = [string]
            else:
                hash_map[key].append(string)
        return list(hash_map.values())

        
        