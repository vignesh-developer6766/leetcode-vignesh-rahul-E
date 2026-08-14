# Last updated: 8/14/2026, 2:49:33 PM
1class Solution:
2    def reverse(self, x):
3        sign = -1 if x < 0 else 1
4        x = abs(x)
5
6        rev = 0
7
8        while x > 0:
9            digit = x % 10
10            rev = rev * 10 + digit
11            x //= 10
12
13        rev *= sign
14
15        if rev < -2**31 or rev > 2**31 - 1:
16            return 0
17
18        return rev