def log_error(message):
    print(f"[Error]: {message}")


def prime_factors_of_N(number):
    nums = []

    if number <= 0:
        log_error("natural numbers only.")
        exit(1)

    for i in range(1, number):
        if prime_numbers.__contains__(number / i):
            if not nums.__contains__(number / i):
                nums.append(number / i)

    return nums


prime_numbers = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]

for i in range(2, 100):
    meter = prime_factors_of_N(i)
    if len(meter) == 1 or len(meter) == 3:
        continue

    if meter[0] > 20 and (meter[1] == 2 or meter[1] == 3):
        continue

    message = f"{i} has prime factors "
    for j in range(len(meter)):
        message += str(f"({int(meter[j])})")
    print(message)
