# Last updated: 9/17/2026, 8:59:55 AM
1class Solution:
2    def findSecondMinimumValue(self, root):
3        first = root.val
4        second = float('inf')
5
6        def dfs(node):
7            nonlocal second
8
9            if not node:
10                return
11
12            if first < node.val < second:
13                second = node.val
14
15            dfs(node.left)
16            dfs(node.right)
17
18        dfs(root)
19
20        return -1 if second == float('inf') else second