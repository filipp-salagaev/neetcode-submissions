class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums2 = []
        num = 1
        for i in range(len(nums)):
            nums2.append(num*nums[i])
            num *= nums[i]
        
        j = len(nums2)-1
        suffprod = 1
        while j > 0:
            nums2[j] = nums2[j-1] * suffprod
            suffprod *= nums[j]
            j-=1
        nums2[0] = suffprod
        return nums2

        
        