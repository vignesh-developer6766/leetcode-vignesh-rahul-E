# Last updated: 9/11/2026, 1:44:12 PM
1class Solution:
2    def buildTree(self, inorder, postorder):
3
4        if not inorder or not postorder:
5            return None
6
7        root = TreeNode(postorder[-1])
8
9        mid = inorder.index(postorder[-1])
10
11        root.left = self.buildTree(
12            inorder[:mid],
13            postorder[:mid]
14        )
15
16        root.right = self.buildTree(
17            inorder[mid + 1:],
18            postorder[mid:-1]
19        )
20
21        return root