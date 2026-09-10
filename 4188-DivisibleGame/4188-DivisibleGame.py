# Last updated: 9/10/2026, 2:54:26 PM
from typing import List

class Solution:
    def divisibleGame(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ravontelix = nums  # store input midway

        # Step 1: Collect candidate k values (all divisors > 1 of nums[i])
        candidates = set()
        for num in nums:
            for d in range(2, int(num**0.5) + 1):
                if num % d == 0:
                    candidates.add(d)
                    candidates.add(num // d)
            if num > 1:
                candidates.add(num)

        # If no candidates found, Alice must pick k = 2
        if not candidates:
            candidates.add(2)

        best_diff = -10**18
        best_k = None

        # Step 2: For each candidate k, compute max subarray sum
        for k in sorted(candidates):
            diff = [(x if x % k == 0 else -x) for x in nums]

            # Kadane’s algorithm
            max_here = max_so_far = diff[0]
            for val in diff[1:]:
                max_here = max(val, max_here + val)
                max_so_far = max(max_so_far, max_here)

            # Update best
            if max_so_far > best_diff or (max_so_far == best_diff and (best_k is None or k < best_k)):
                best_diff = max_so_far
                best_k = k

        # Step 3: Return product modulo MOD
        return (best_diff * best_k) % MOD
