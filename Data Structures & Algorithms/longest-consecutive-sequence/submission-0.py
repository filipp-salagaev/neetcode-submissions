class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        longest = 1
        num = nums[0]
        for num1 in nums:
            leng = 1
            if num1 - 1 not in s:
                curr = num1
                while curr+1 in s:
                    curr += 1
                    leng += 1
            longest = max(longest, leng)
            
        
        return longest
                