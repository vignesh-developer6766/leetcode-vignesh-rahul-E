# Last updated: 9/11/2026, 1:31:56 PM
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = Counter(arr)
        freqs = list(freq.values())
        return len(freqs) == len(set(freqs))