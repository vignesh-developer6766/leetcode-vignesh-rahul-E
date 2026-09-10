# Last updated: 9/10/2026, 2:55:36 PM
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse