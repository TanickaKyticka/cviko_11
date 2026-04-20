
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