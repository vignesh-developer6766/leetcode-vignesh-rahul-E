# Last updated: 9/11/2026, 1:41:50 PM
1from collections import deque
2
3class Solution:
4    def levelOrder(self, root):
5        if root is None:
6            return []
7
8        result = []
9        queue = deque([root])
10
11        while queue:
12            level = []
13
14            for _ in range(len(queue)):
15                node = queue.popleft()
16
17                level.append(node.val)
18
19                if node.left:
20                    queue.append(node.left)
21
22                if node.right:
23                    queue.append(node.right)
24
25            result.append(level)
26
27        return result