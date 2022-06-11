import random

number_of_streaks = 0

for experiment in range(10000):
    coins = [random.choice(["H", "T"]) for _ in range(100)]
    for i in range(len(coins)):
        if coins[i : i + 6] == ["H"] * 6 or coins[i : i + 6] == ["T"] * 6:
            number_of_streaks += 1
            break

print(f"{number_of_streaks / 10000 * 100}%")
