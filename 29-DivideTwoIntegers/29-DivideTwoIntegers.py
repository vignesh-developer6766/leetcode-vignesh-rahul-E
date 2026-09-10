# Last updated: 9/10/2026, 2:55:22 PM
class Solution:
    def divide(self, dividend, divisor):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Find the largest multiple of divisor
        # that can be subtracted from dividend
        while dividend >= divisor:

            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        # 32-bit range check
        if quotient > INT_MAX:
            return INT_MAX

        if quotient < INT_MIN:
            return INT_MIN

        return quotient