# Last updated: 9/11/2026, 1:32:15 PM
from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        counts = Counter(deck).values()
        return reduce(gcd, counts) > 1