# Last updated: 8/14/2026, 3:01:15 PM
1class Solution:
2    def postorderTraversal(self, root):
3        result = []
4
5        def dfs(node):
6            if not node:
7                return
8
9            dfs(node.left)
10            dfs(node.right)
11            result.append(node.val)
12
13        dfs(root)
14
15        return result