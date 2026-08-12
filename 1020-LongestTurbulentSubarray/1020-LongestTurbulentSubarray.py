# Last updated: 8/12/2026, 12:21:32 PM
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        max_len = 1
        curr    = 1
        
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            
            if diff == 0:
                curr = 1                      # equal → reset to 1
            elif i == 1:
                curr = 2                      # first pair always starts streak
            else:
                prev_diff = arr[i-1] - arr[i-2]
                # turbulent if signs are opposite
                if (diff > 0) != (prev_diff > 0):
                    curr += 1
                else:
                    curr = 2                  # reset but keep current pair
            
            max_len = max(max_len, curr)
        
        return max_len