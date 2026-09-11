# Last updated: 9/11/2026, 1:39:25 PM
1class Solution:
2    def recoverTree(self, root):
3
4        first = None
5        second = None
6        prev = None
7
8        def inorder(node):
9            nonlocal first, second, prev
10
11            if node is None:
12                return
13
14            inorder(node.left)
15
16            if prev and prev.val > node.val:
17
18                if first is None:
19                    first = prev
20
21                second = node
22
23            prev = node
24
25            inorder(node.right)
26
27        inorder(root)
28
29        first.val, second.val = second.val, first.val