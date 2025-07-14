class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[i][j] = número de formas de fazer a quantia j usando as primeiras i moedas
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Caso base: há 1 forma de fazer valor 0 (sem usar moedas)
        for i in range(n + 1):
            dp[i][0] = 1

        # Preenche a tabela
        for i in range(1, n + 1):  # moedas 1 até n
            coin = coins[i - 1]
            for j in range(amount + 1):  # valores de 0 até amount
                # Não usar a moeda atual
                dp[i][j] = dp[i - 1][j]
                # Usar a moeda atual (quantas vezes quiser)
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]
        
        return dp[n][amount]
