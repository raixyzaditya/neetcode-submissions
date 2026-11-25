class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        l = len(coins)
        prev = [0 for _ in range(total+1)]
        prev[0] = 1
        for i in range(l-1,-1,-1):
            curr = [0 for _ in range(total+1)]
            curr[0] = 1
            for j in range(total+1):
                np = prev[j]
                p = 0
                if j >= coins[i]:
                    p = curr[j-coins[i]]
                curr[j] = np+p
            prev = curr
        return prev[total]
        # dp = [[0 for _ in range(total+1)] for _ in range(l+1)]

        # for i in range(l-1,-1,-1):
        #     for j in range(total + 1):
        #         if j == 0:
        #             dp[i][0] = 1
        #         else:
        #          not_picked = dp[i+1][j]
        #          picked = 0
        #          if j >= coins[i]:
        #             picked = dp[i][j-coins[i]]
        #          dp[i][j] = not_picked + picked
        # return dp[0][total]

        # l = len(coins)
        # def f(idx,amount):
        #     if amount == 0:
        #         return 1
        #     if idx == l:
        #         return 0
        #     if (idx,amount) in dp:
        #         return dp[(idx,amount)]
        #     not_picked = 0 + f(idx+1,amount)
        #     picked = 0
        #     if amount >= coins[idx]:
        #         picked = f(idx,amount-coins[idx])
        #     dp[(idx,amount)] = not_picked + picked
        #     return dp[(idx,amount)]
        # return f(0,total)
            
            
        