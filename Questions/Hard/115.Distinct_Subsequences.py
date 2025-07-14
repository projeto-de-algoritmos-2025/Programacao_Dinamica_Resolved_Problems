class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        dp = [0] * (n2 + 1)
        dp[n2] = 1  # Base: uma forma de formar string vazia de t a partir de s

        for i in range(n1 - 1, -1, -1):  # Percorre s de trás para frente
            # Usamos uma cópia temporária para simular a linha anterior
            next_dp = dp[:]
            for j in range(n2):
                if s[i] == t[j]:
                    next_dp[j] += dp[j + 1]
            dp = next_dp
        
        return dp[0]
