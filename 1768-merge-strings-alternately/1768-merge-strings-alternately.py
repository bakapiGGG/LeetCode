class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        if len(word1) == len(word2):
            for i in range(len(word1)):
                merged += word1[i]
                merged += word2[i]

        elif len(word1) > len(word2):
            for i in range(len(word2)):
                merged += word1[i]
                merged += word2[i]

            merged += word1[len(word2):]
        
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                merged += word1[i]
                merged += word2[i]

            merged += word2[len(word1):]

        return merged


            

