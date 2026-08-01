from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        dct = dict()

        for key,v in cnt.items():
            if v in dct:
                dct[v].append(key)
            else:
                dct[v] = [key]
        
        elems = 0
        to_return = []
        for freq in range(len(nums), 0, -1):
            if elems == k:
                break
            if freq in dct:
                for num in dct[freq]:
                    if elems == k:
                        break
                    to_return.append(num)
                    elems += 1
        
        return to_return
            


