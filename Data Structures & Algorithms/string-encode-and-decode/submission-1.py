class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for string in strs:
            newstr += str(len(string)) + "#" + string
        return newstr
    
    def decode(self, s: str) -> List[str]:
        newlist = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            nextstr = s[j + 1:j + 1 + length]
            newlist.append(nextstr)
            i = j + 1 + length

        return newlist

