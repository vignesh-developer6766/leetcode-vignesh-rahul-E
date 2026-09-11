# Last updated: 9/11/2026, 1:40:54 PM
1class Solution:
2    def isSymmetric(self, root):
3
4        def mirror(left, right):
5
6            if left is None and right is None:
7                return True
8
9            if left is None or right is None:
10                return False
11
12            if left.val != right.val:
13                return False
14
15            return (
16                mirror(left.left, right.right)
17                and
18                mirror(left.right, right.left)
19            )
20
21        return mirror(root.left, root.right)