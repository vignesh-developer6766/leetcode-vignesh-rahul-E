# Last updated: 9/11/2026, 1:38:45 PM
1class Solution:
2    def isValidBST(self, root):
3
4        def validate(node, low, high):
5            if node is None:
6                return True
7
8            if node.val <= low or node.val >= high:
9                return False
10
11            return (
12                validate(node.left, low, node.val)
13                and
14                validate(node.right, node.val, high)
15            )
16
17        return validate(root, float("-inf"), float("inf"))