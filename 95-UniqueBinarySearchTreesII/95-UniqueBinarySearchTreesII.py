# Last updated: 9/11/2026, 1:35:51 PM
1class Solution:
2    def generateTrees(self, n):
3        def build(start, end):
4            if start > end:
5                return [None]
6
7            result = []
8
9            for root in range(start, end + 1):
10
11                left_trees = build(start, root - 1)
12                right_trees = build(root + 1, end)
13
14                for left in left_trees:
15                    for right in right_trees:
16
17                        node = TreeNode(root)
18                        node.left = left
19                        node.right = right
20
21                        result.append(node)
22
23            return result
24
25        return build(1, n)