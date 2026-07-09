class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        hm = {}
        length = 0
        maxlen = 0
        while j < len(s):
            if s[j] in hm:
                if length > maxlen:
                    maxlen = length
                if hm[s[j]] + 1 >= i:
                    i = hm[s[j]] + 1
                hm[s[j]] = j
                length = j+1-i
            else:
                hm[s[j]] = j
                length += 1
                if length > maxlen:
                    maxlen = length
            j+=1
        
        return maxlen

