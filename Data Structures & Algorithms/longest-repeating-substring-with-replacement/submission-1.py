class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 0
        maxlen = 0
        freq = defaultdict(int)
        maxFreq = 0
        while j < len(s):
            freq[s[j]] += 1
            maxFreq = max(maxFreq, freq[s[j]])
                
            while (j - i + 1) - maxFreq > k:
                freq[s[i]]-=1
                i+=1

            maxlen = max(maxlen, j-i+1)
            j+=1

        return maxlen