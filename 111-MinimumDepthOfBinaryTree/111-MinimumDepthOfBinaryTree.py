# Last updated: 9/11/2026, 1:32:42 PM
class Solution:
    def minDepth(self, root):

        if root is None:
            return 0

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return 1 + min(left, right)