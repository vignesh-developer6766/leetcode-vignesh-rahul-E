# Last updated: 8/12/2026, 12:20:34 PM
class Solution:
    def maxDistance(self, moves: str) -> int:
        up = moves.count('U')
        down = moves.count('D')
        left = moves.count('L')
        right = moves.count('R')
        wild = moves.count('_')
        
        x = right - left
        y = up - down
        
        return abs(x) + abs(y) + wild
