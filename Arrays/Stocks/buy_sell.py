def buy_sell(arr: list[int]) -> int:
    mini = arr[0]
    profit = 0
    for i in range(len(arr)):
        cost = arr[i] - mini
        profit = max(profit, cost)
        mini = min(mini, arr[i])

    return profit

def main():
    arr = [7, 1, 5, 3, 6, 4]
    ans = buy_sell(arr)
    print(f"You can make a profit of {ans}")

if __name__ == "__main__":
    main()