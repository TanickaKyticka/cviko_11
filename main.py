
from sorting import bubble_sort, selection_sort
import random

from student_grades import StudentsGrades
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

seznam = [5, 1, 4, 2, 8]
print(f"Puvodni seznam:" , seznam)
print(f"Serazeny seznam:", selection_sort(seznam))
print(f"Bubbles:", bubble_sort(seznam))


results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
print(results.get_grade(2))  # A (91 bodů)
print(results.get_grade(6))  # A (100 bodů)
print(results.get_grade(7))  # F (38 bodů)

print(results.find(100))  # [6]
print(results.find(50))   # [4]
print(results.find(77))   # []

print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print("Pocet studentu:", results.count())

    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    print("Studenti se 100 body:", results.find(100))

    print("Serazené vysledky:", results.get_sorted())


if __name__ == "__main__":
    main()

# #bonus1
# def average(self):
#     return sum(self.scores) / len(self.scores)
#
#
# def best(self):
#     return max(self.scores)
#
#
# def worst(self):
#     return min(self.scores)
#
#
# def pass_rate(self):
#     passed = 0
#     for score in self.scores:
#         if score >= 50:
#             passed += 1
#     return passed / len(self.scores)
#
#
# def __str__(self):
#     return f"StudentsGrades: {self.count()} studentu, prumer {self.average():.1f}"

#bonus2
def __init__(self, scores):
    self.scores = scores
    self._sorted_scores = None


def find_sorted(self, score):
    if self._sorted_scores is None:
        print("sorting…")
        self._sorted_scores = self.get_sorted()

    left = 0
    right = len(self._sorted_scores) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = self._sorted_scores[mid]

        if mid_value == score:
            return mid
        elif mid_value < score:
            left = mid + 1
        else:
            right = mid - 1

    return None
