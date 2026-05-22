Student's Code: "class Solution:
      def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

s = Solution()
assert s.findKthLargest([3,2,1,5,6,4], 2) == 5"
