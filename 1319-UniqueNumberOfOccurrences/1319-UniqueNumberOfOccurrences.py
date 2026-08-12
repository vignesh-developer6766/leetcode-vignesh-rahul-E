# Last updated: 8/12/2026, 12:21:21 PM
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = Counter(arr)
        freqs = list(freq.values())
        return len(freqs) == len(set(freqs))