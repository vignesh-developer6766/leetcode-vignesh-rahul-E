# Last updated: 9/11/2026, 1:32:10 PM
class Solution:
    def reorderLogFiles(self, logs):
        def key(log):
            identifier, rest = log.split(" ", 1)

            if rest[0].isalpha():  # Letter-log
                return (0, rest, identifier)
            else:                  # Digit-log
                return (1,)

        return sorted(logs, key=key)