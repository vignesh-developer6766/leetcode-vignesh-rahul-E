# Last updated: 9/17/2026, 10:00:41 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        count = {}
4
5        for ch in s:
6            count[ch] = count.get(ch, 0) + 1
7
8        length = 0
9        odd = False
10
11        for value in count.values():
12            length += (value // 2) * 2
13
14            if value % 2 == 1:
15                odd = True
16
17        if odd:
18            length += 1
19
20        return length