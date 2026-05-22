student's code = '''
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
s = Solution()
assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
    '''
