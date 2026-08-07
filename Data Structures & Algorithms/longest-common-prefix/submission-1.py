class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i in range(len(strs[0])):
            count = 0
            curr = strs[0][i]
            for string in strs:
                if len(string) <= i:
                    return pref
                if curr == string[i]:
                    count+=1
                    if count == len(strs):
                        pref += curr
                    continue
                else:
                    return pref
        return pref
