# Last updated: 9/10/2026, 3:01:50 PM
1class Solution:
2    def sortedArrayToBST(self, nums):
3        if not nums:
4            return None
5
6        mid = len(nums) // 2
7
8        root = TreeNode(nums[mid])
9
10        root.left = self.sortedArrayToBST(nums[:mid])
11        root.right = self.sortedArrayToBST(nums[mid + 1:])
12
13        return root