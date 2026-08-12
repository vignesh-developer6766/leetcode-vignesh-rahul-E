# Last updated: 8/12/2026, 12:21:28 PM
from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        row_count  = defaultdict(int)
        col_count  = defaultdict(int)
        diag_count = defaultdict(int)  # row - col
        anti_count = defaultdict(int)  # row + col
        
        lamp_set = set()
        
        # Turn on lamps (deduplicate)
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))
                row_count[r]       += 1
                col_count[c]       += 1
                diag_count[r - c]  += 1
                anti_count[r + c]  += 1
        
        ans = []
        
        for qr, qc in queries:
            # Check illumination
            illuminated = (
                row_count[qr]        > 0 or
                col_count[qc]        > 0 or
                diag_count[qr - qc]  > 0 or
                anti_count[qr + qc]  > 0
            )
            ans.append(1 if illuminated else 0)
            
            # Turn off the queried cell + 8 neighbors
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = qr + dr, qc + dc
                    if (nr, nc) in lamp_set:
                        lamp_set.remove((nr, nc))
                        row_count[nr]      -= 1
                        col_count[nc]      -= 1
                        diag_count[nr - nc] -= 1
                        anti_count[nr + nc] -= 1
        
        return ans