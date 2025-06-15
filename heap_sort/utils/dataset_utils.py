import random


def generate_sorted_dataset(size):
    """Generates a sorted dataset."""
    return list(range(size))


def generate_reverse_sorted_dataset(size):
    """Generates a reverse sorted dataset."""
    return list(range(size, 0, -1))


def generate_random_dataset(size, lower=0, upper=1000):
    """Generates a random dataset."""
    return [random.randint(lower, upper) for _ in range(size)]
