# Last updated: 8/12/2026, 12:21:50 PM
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # prefix_sum -> first index it was seen
        first_seen = {0: -1}   # sum=0 exists before index 0
        
        max_len    = 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            
            if prefix_sum in first_seen:
                max_len = max(max_len, i - first_seen[prefix_sum])
            else:
                first_seen[prefix_sum] = i   # only store FIRST occurrence
        
        return max_len