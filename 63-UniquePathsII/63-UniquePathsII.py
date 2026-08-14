# Last updated: 8/14/2026, 3:59:51 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid):
3        m = len(obstacleGrid)
4        n = len(obstacleGrid[0])
5
6        dp = [0] * n
7        dp[0] = 1
8
9        for i in range(m):
10            for j in range(n):
11
12                if obstacleGrid[i][j] == 1:
13                    dp[j] = 0
14
15                elif j > 0:
16                    dp[j] = dp[j] + dp[j - 1]
17
18        return dp[n - 1]