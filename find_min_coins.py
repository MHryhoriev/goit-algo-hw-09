def find_min_coins(nominal_values: list, total_sum: int):
    """
    Finds the minimum number of coins required to make up a given sum using a dynamic programming approach.
    """
    min_coins, last_coin = initialize_dp_arrays(total_sum)
    fill_dp_arrays(nominal_values, total_sum, min_coins, last_coin)
    return reconstruct_solution(total_sum, last_coin)

def reconstruct_solution(total_sum: int, last_coin: list):
    """
    Reconstructs the solution from the last_coin array, counting the number of each coin used.
    """
    result = {}
    current_sum = total_sum
    while current_sum > 0 and last_coin[current_sum] != -1:
        coin = last_coin[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin
    
    if current_sum > 0:
        return "No solution possible with given coin denominations"
    return result

def initialize_dp_arrays(total_sum: int):
    """
    Initializes the min_coins and last_coin arrays for dynamic programming.
    """
    min_coins = [float('inf')] * (total_sum + 1)
    min_coins[0] = 0
    last_coin = [-1] * (total_sum + 1)
    return min_coins, last_coin


def fill_dp_arrays(nominal_values: list, total_sum: int, min_coins: list, last_coin: list):
    """
    Fills in the min_coins and last_coin arrays based on the minimum number of coins required.
    """
    for amount in range(1, total_sum + 1):
        for coin in nominal_values:
            if amount >= coin and min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1
                last_coin[amount] = coin