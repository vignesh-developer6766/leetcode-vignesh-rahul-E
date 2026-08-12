# Last updated: 8/12/2026, 12:21:37 PM
from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        counts = Counter(deck).values()
        return reduce(gcd, counts) > 1