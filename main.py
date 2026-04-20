
from sorting import bubble_sort, selection_sort
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

seznam = [5, 1, 4, 2, 8]
print(f"Puvodni seznam:" , seznam)
print(f"Serazeny seznam:", selection_sort(seznam))
print(f"Bubbles:", bubble_sort(seznam))