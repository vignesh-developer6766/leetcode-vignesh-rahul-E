# Last updated: 8/12/2026, 12:21:55 PM
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        res = [0] * n
        enum = list(enumerate(nums))  # (index, value)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            merged = []
            i = j = 0
 
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    merged.append(right[j])
                    j += 1
                else:
                    res[left[i][0]] += len(right) - j
                    merged.append(left[i])
                    i += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        merge_sort(enum)
        return res
