# Last updated: 8/12/2026, 12:21:19 PM
class Solution:
    def mctFromLeafValues(self, arr):
        stack = [float('inf')]
        res = 0

        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                res += mid * min(stack[-1], num)
            stack.append(num)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res