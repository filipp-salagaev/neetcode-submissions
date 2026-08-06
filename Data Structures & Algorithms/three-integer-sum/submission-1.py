class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        i = 0
        j = i+1
        triplets = set()
        for i in range(len(nums)):
            target = -nums[i]
            seen = {}
            for j in range(i+1, len(nums)):
                if (target - nums[j]) in seen:
                    if ((nums[i], nums[seen[target - nums[j]]], nums[j])) not in triplets:
                        triplets.add((nums[i], nums[seen[target - nums[j]]], nums[j]))
                else:
                    seen[nums[j]] = j
        return [list(t) for t in triplets]