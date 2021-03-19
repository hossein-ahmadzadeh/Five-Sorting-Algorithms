from time import time
from random import uniform


def generate_array(num):
    my_list = []
    for i in range(num):
        my_list.append(int(uniform(1, num)))
    return my_list


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


my_array = generate_array(1000)

t1 = time()

quick_sort(my_array)

t2 = time()

print(f"It took {t2 - t1} seconds!")

print("***********************************************************")

my_array = generate_array(10000)

t1 = time()

quick_sort(my_array)

t2 = time()

print(f"It took {t2 - t1} seconds!")

print("***********************************************************")

my_array = generate_array(100000)

t1 = time()

quick_sort(my_array)

t2 = time()

print(f"It took {t2 - t1} seconds!")

print("***********************************************************")
