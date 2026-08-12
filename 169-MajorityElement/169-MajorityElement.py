# Last updated: 8/12/2026, 12:22:28 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]