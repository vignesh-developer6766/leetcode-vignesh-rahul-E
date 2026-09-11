# Last updated: 9/11/2026, 1:31:58 PM
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