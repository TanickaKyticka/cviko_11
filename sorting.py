#ukol1
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam):
    seznam = seznam[:]
    for pozice_ukladani in range(len(seznam)):
        min_idx = pozice_ukladani
        for pozice_prochazena in range(pozice_ukladani + 1, len(seznam)):
            if seznam[pozice_prochazena] < seznam[min_idx]:
                min_idx=pozice_prochazena
        seznam[pozice_ukladani], seznam[min_idx] = seznam[min_idx], seznam[pozice_ukladani]
    return seznam


#ukol2
def bubble_sort(seznamek):
    seznamek = seznamek.copy()

    n = len(seznamek)

    for i in range(n):
        for j in range(0, n - i - 1):
            if seznamek[j] > seznamek[j + 1]:
                seznamek[j], seznamek[j + 1] = seznamek[j + 1], seznamek[j]

    return seznamek

#ukol3
