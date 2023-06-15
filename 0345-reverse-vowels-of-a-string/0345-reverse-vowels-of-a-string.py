class Solution:
    def reverseVowels(self, s: str) -> str:

        string = list(s)
        pos_list = []
        char_list = []

        for pos, char in enumerate(s):

            if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                pos_list.append(pos)
                char_list.append(char)

        char_list.reverse()

        i = 0



        for pos, char in enumerate(s):

            if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:

                string[pos] = char_list[i]

                i+= 1

        final_string = "".join(string)
        
        return final_string

