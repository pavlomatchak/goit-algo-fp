import matplotlib.pyplot as plt
import random

def calculate_probabilities():
    nums = 100_000
    counts = {i: 0 for i in range(2, 13)}

    for _ in range(nums):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        counts[dice_one + dice_two] += 1

    return {key: count / nums for key, count in counts.items()}

def show_graph(table, prob, keys):
    plt.bar(keys, prob, color='blue', alpha=0.5, label='Calculated')
    plt.bar(keys, table, color='red', alpha=0.5, align='edge', width=0.5, label='Table')
    plt.legend()
    plt.xlabel('Number')
    plt.ylabel('Probability')
    plt.xticks(keys)
    plt.show()

table_data = {
    2: 0.0278,
    3: 0.0556,
    4: 0.0833,
    5: 0.1111,
    6: 0.1389,
    7: 0.1667,
    8: 0.1389,
    9: 0.1111,
    10: 0.0833,
    11: 0.0556,
    12: 0.0278,
}
table_values = list(table_data.values())
prob_values = list(calculate_probabilities().values())
keys = list(table_data.keys())

show_graph(table_values, prob_values, keys)
