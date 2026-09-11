# Last updated: 9/11/2026, 1:36:48 PM
1class Solution:
2    def numTrees(self, n):
3        dp = [0] * (n + 1)
4
5        dp[0] = 1
6        dp[1] = 1
7
8        for nodes in range(2, n + 1):
9            for root in range(1, nodes + 1):
10                left = root - 1
11                right = nodes - root
12
13                dp[nodes] += dp[left] * dp[right]
14
15        return dp[n]