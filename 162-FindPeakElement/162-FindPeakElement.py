# Last updated: 8/12/2026, 12:22:30 PM
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                # Peak is on the right side
                left = mid + 1
            else:
                # Peak is on the left side (including mid)
                right = mid
        
        return left  # or right, since they converge
