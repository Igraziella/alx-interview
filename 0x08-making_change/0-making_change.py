#!/usr/bin/python3
"""Method to determine fewest no of coins"""

def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet
    a given total
    """
    if total < 0:
        return -1
    
    # Create a list to store the minimum number of coins for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    
    # Base case: Zero coins are needed to make a total of 0
    dp[0] = 0
    
    # Iterate through all possible totals from 1 to 'total'
    for i in range(1, total + 1):
        # Iterate through all coin values
        for coin in coins:
            # Check if the coin value is less than or equal to the current total
            if coin <= i:
                # Update the minimum number of coins needed for the current total
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means the total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]