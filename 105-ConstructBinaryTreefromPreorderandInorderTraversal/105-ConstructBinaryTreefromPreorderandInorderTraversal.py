# Last updated: 9/11/2026, 1:43:28 PM
1class Solution:
2    def buildTree(self, preorder, inorder):
3
4        if not preorder or not inorder:
5            return None
6
7        root = TreeNode(preorder[0])
8
9        mid = inorder.index(preorder[0])
10
11        root.left = self.buildTree(
12            preorder[1:mid + 1],
13            inorder[:mid]
14        )
15
16        root.right = self.buildTree(
17            preorder[mid + 1:],
18            inorder[mid + 1:]
19        )
20
21        return root