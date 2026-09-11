# Last updated: 9/11/2026, 1:31:32 PM
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
