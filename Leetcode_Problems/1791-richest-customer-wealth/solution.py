class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total_wealth = []
        
        for i in range(len(accounts)):
            total_wealth.append(sum(accounts[i]))
        return max(total_wealth)
