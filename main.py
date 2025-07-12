from typing import List, Dict

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> Dict[int, int]:
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result


def find_min_coins(amount: int) -> Dict[int, int]:
    # min_coins[i] = мінімальна кількість монет для суми i
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # last_coin[i] = остання монета, яку використали для побудови суми i
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    # Відновлення словника з монетами
    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


if __name__ == "__main__":
    amount = 113
    print("Greedy:", find_coins_greedy(amount))
    print("DP:", find_min_coins(amount))
