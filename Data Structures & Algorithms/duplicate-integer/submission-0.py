class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = []

        for i in range(len(nums)):
            if nums[i] in list1:
                return True
            else:
                list1.append(nums[i])

        return False 