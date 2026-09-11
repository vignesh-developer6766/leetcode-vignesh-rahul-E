# Last updated: 9/11/2026, 1:38:07 PM
1class Solution:
2    def isInterleave(self, s1, s2, s3):
3        if len(s1) + len(s2) != len(s3):
4            return False
5
6        dp = [False] * (len(s2) + 1)
7        dp[0] = True
8
9        for j in range(1, len(s2) + 1):
10            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
11
12        for i in range(1, len(s1) + 1):
13            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
14
15            for j in range(1, len(s2) + 1):
16                dp[j] = (
17                    (dp[j] and s1[i - 1] == s3[i + j - 1])
18                    or
19                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
20                )
21
22        return dp[len(s2)]