# Last updated: 9/10/2026, 3:00:38 PM
1class Solution:
2    def maxDepth(self, root):
3        if root is None:
4            return 0
5
6        left = self.maxDepth(root.left)
7        right = self.maxDepth(root.right)
8
9        return 1 + max(left, right)