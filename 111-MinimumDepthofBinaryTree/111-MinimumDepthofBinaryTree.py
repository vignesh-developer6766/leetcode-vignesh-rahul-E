# Last updated: 9/10/2026, 3:05:22 PM
1class Solution:
2    def minDepth(self, root):
3
4        if root is None:
5            return 0
6
7        if root.left is None:
8            return 1 + self.minDepth(root.right)
9
10        if root.right is None:
11            return 1 + self.minDepth(root.left)
12
13        left = self.minDepth(root.left)
14        right = self.minDepth(root.right)
15
16        return 1 + min(left, right)