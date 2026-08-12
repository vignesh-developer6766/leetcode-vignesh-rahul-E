# Last updated: 8/12/2026, 12:21:51 PM
class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        answer = [""] * n

        sorted_scores = sorted(
            [(s, i) for i, s in enumerate(score)],
            reverse=True
        )

        for rank, (_, idx) in enumerate(sorted_scores, start=1):
            if rank == 1:
                answer[idx] = "Gold Medal"
            elif rank == 2:
                answer[idx] = "Silver Medal"
            elif rank == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(rank)

        return answer