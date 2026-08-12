# Last updated: 8/12/2026, 12:22:48 PM
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all are in place
        return n + 1
