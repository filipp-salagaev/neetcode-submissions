from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = Counter(nums)

        for item, count in hm.items():
            if count > 1:
                return True

        return False 