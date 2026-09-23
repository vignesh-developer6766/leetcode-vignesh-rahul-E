# Last updated: 9/23/2026, 9:53:09 AM
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w = int(area ** 0.5)

        while area % w != 0:
            w -= 1

        return [area // w, w]