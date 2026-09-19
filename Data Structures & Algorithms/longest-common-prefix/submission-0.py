class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #create a master list which would store all the other lists
        all_char_lists = []

        #make individual lists for characters for each word in strs
        for index, element in enumerate(strs):
            print(index, element)
            character_list = []
            for character in element:
                character_list.append(character)

            all_char_lists.append(character_list)

        shortest_word_len = min(len(character_list) for character_list in all_char_lists)

        longest_prefix = []

        for col in range(shortest_word_len):
            current_char = all_char_lists[0][col]

            for row in range(1, len(all_char_lists)):
                if all_char_lists[row][col] != current_char:
                    return "".join(longest_prefix)
            
            longest_prefix.append(current_char)
        return "".join(longest_prefix) 