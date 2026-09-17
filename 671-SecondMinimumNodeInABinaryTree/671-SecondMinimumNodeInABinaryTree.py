# Last updated: 9/17/2026, 9:00:27 AM
class Solution:
    def findSecondMinimumValue(self, root):
        first = root.val
        second = float('inf')

        def dfs(node):
            nonlocal second

            if not node:
                return

            if first < node.val < second:
                second = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return -1 if second == float('inf') else second