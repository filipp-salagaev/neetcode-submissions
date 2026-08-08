class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        length = 0
        if len(word1) < len(word2):
            word = word2
            length = len(word1)
        else:
            word = word1
            length = len(word2)
        new_str = ""
        for i in range(length):
            new_str += word1[i]
            new_str += word2[i]

        new_str += word[length:]
        return new_str