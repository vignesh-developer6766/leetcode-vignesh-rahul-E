# Last updated: 9/11/2026, 1:34:56 PM
1class Solution:
2    def inorderTraversal(self, root):
3        result = []
4
5        def inorder(node):
6            if node is None:
7                return
8
9            inorder(node.left)       # Left
10            result.append(node.val)  # Root
11            inorder(node.right)      # Right
12
13        inorder(root)
14        return result