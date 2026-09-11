# Last updated: 9/11/2026, 1:42:29 PM
1from collections import deque
2
3class Solution:
4    def zigzagLevelOrder(self, root):
5        if root is None:
6            return []
7
8        result = []
9        queue = deque([root])
10        left_to_right = True
11
12        while queue:
13            level = []
14
15            for _ in range(len(queue)):
16                node = queue.popleft()
17                level.append(node.val)
18
19                if node.left:
20                    queue.append(node.left)
21
22                if node.right:
23                    queue.append(node.right)
24
25            if not left_to_right:
26                level.reverse()
27
28            result.append(level)
29
30            left_to_right = not left_to_right
31
32        return result