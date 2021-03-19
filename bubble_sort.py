from time import time
from random import uniform


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        return f"It took {t2 - t1} seconds!"
    return wrapper


def generate_array(num):
    my_list = []
    for i in range(num):
        my_list.append(int(uniform(1, num)))
    return my_list


@performance
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


my_array = generate_array(1000)

print(bubble_sort(my_array))

print("***********************************************************")

my_array = generate_array(10000)

print(bubble_sort(my_array))

print("***********************************************************")

my_array = generate_array(100000)

print(bubble_sort(my_array))

print("***********************************************************")
