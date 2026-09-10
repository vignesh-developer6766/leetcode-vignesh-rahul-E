# Last updated: 9/10/2026, 3:04:03 PM
1class Solution:
2    def isBalanced(self, root):
3
4        def height(node):
5
6            if node is None:
7                return 0
8
9            left = height(node.left)
10
11            if left == -1:
12                return -1
13
14            right = height(node.right)
15
16            if right == -1:
17                return -1
18
19            if abs(left - right) > 1:
20                return -1
21
22            return 1 + max(left, right)
23
24        return height(root) != -1