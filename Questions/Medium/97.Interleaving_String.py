class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

        if len_s1 + len_s2 != len_s3:
            return False

        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        dp[0][0] = True

        for i in range(len_s1 + 1):
            for j in range(len_s2 + 1):
                k = i + j - 1 

                if i > 0 and s1[i - 1] == s3[k] and dp[i - 1][j]:
                    dp[i][j] = True
                if j > 0 and s2[j - 1] == s3[k] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[len_s1][len_s2]
