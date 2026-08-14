# Last updated: 8/14/2026, 2:57:59 PM
1class Solution:
2    def search(self, nums, target):
3        left = 0
4        right = len(nums) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if nums[mid] == target:
10                return True
11
12            # Cannot determine which side is sorted
13            if nums[left] == nums[mid] == nums[right]:
14                left += 1
15                right -= 1
16
17            elif nums[left] <= nums[mid]:
18                # Left side is sorted
19                if nums[left] <= target < nums[mid]:
20                    right = mid - 1
21                else:
22                    left = mid + 1
23
24            else:
25                # Right side is sorted
26                if nums[mid] < target <= nums[right]:
27                    left = mid + 1
28                else:
29                    right = mid - 1
30
31        return False