class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        while val in nums:
            nums.remove(val)
            k -= 1
        return k