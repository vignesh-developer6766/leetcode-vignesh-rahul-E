# Last updated: 9/11/2026, 1:32:47 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        words = s.split()
4
5        if len(pattern) != len(words):
6            return False
7
8        p_to_w = {}
9        w_to_p = {}
10
11        for p, w in zip(pattern, words):
12
13            if p in p_to_w and p_to_w[p] != w:
14                return False
15
16            if w in w_to_p and w_to_p[w] != p:
17                return False
18
19            p_to_w[p] = w
20            w_to_p[w] = p
21
22        return True