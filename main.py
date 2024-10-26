from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

def main():

    nominal_values = [50, 25, 10, 5, 2, 1]

    greedy_algorithm = find_coins_greedy(nominal_values, 113)
    print(f"Greedy algorithm function: {greedy_algorithm}")

    dynamic_programming_algorithm = find_min_coins(nominal_values, 113)
    print(f"Dynamic programming function: {dynamic_programming_algorithm}")

if __name__ == "__main__":
    main()
