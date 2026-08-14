# Last updated: 8/14/2026, 2:47:38 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s):
3        chars = set()
4        left = 0
5        max_length = 0
6
7        for right in range(len(s)):
8            while s[right] in chars:
9                chars.remove(s[left])
10                left += 1
11
12            chars.add(s[right])
13
14            max_length = max(max_length, right - left + 1)
15
16        return max_length