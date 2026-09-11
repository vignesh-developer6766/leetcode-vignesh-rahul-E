# Last updated: 9/11/2026, 1:31:50 PM
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