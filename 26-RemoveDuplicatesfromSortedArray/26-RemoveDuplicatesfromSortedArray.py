# Last updated: 8/14/2026, 2:53:14 PM
1class Solution:
2    def removeDuplicates(self, nums):
3        k = 1
4
5        for i in range(1, len(nums)):
6            if nums[i] != nums[k - 1]:
7                nums[k] = nums[i]
8                k += 1
9
10        return k