from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:
            current = dp.copy()

            for diff, shorter_sum in current.items():
                taller_sum = shorter_sum + diff

                new_diff = diff + rod
                dp[new_diff] = max(dp.get(new_diff, 0), shorter_sum)

                new_shorter_sum = shorter_sum + rod
                new_diff = abs(taller_sum - new_shorter_sum)
                dp[new_diff] = max(dp.get(new_diff, 0), min(new_shorter_sum, taller_sum))

        return dp.get(0, 0)