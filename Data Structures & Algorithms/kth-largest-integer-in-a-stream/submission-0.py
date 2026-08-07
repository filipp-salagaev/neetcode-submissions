import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        heap = nums[-k:]
        heapq.heapify(heap)
        self.nums = heap
        self.k = k
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]