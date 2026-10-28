"""Intentionally buggy code for a debugging demonstration."""

def average(numbers):
    total = 0
    # Bug: this loop stops before the last item.
    for index in range(0, len(numbers) - 1):
        total += numbers[index]
    # Bug: empty lists cause division by zero.
    return total / len(numbers)


if __name__ == "__main__":
    values = [10, 20, 30, 40]
    print("Average:", average(values))
