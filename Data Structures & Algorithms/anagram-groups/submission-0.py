from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for i in range(len(strs)):
            count = [0] * 26
            for c in strs[i]:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in dictionary:
                dictionary[tuple(count)].append(strs[i])
            else:
                dictionary[tuple(count)] = [strs[i]]

        return list(dictionary.values())

        