# Last updated: 8/12/2026, 12:20:38 PM
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(f for f in freq.values() if f == max_freq)