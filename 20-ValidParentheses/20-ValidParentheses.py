# Last updated: 8/12/2026, 12:22:55 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in mapping:  # closing bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:  # opening bracket
                stack.append(char)

        return not stack
