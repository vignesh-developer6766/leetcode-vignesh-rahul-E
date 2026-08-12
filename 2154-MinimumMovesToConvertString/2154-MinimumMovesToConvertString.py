# Last updated: 8/12/2026, 12:21:11 PM
class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        i = 0

        while i < len(s):
            if s[i] == 'X':
                count += 1
                i += 3
            else:
                i += 1

        return count