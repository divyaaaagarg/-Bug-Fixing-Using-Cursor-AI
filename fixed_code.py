"""Corrected average calculation with clear input validation."""

def average(numbers: list[float]) -> float:
    """Return the arithmetic mean; reject an empty list."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    samples = [10, 20, 30, 40]
    print("Average:", average(samples))

    try:
        print(average([]))
    except ValueError as error:
        print(f"Input error: {error}")
