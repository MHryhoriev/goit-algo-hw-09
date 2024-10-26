def get_coin_count(remaining_sum, value):
    """
    Calculates the maximum count of coins of a specific denomination that can fit into the remaining sum.
    """
    count = remaining_sum // value
    remaining_sum -= count * value
    return count, remaining_sum

def find_coins_greedy(nominal_values: list, total_sum: int):
    """
    Finds the minimum number of coins required to make up a given sum using a greedy approach.
    """
    result = {}
    
    for value in nominal_values:
        count, total_sum = get_coin_count(total_sum, value)
        if count > 0:
            result[value] = count

    return result