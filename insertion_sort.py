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
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


my_array = generate_array(1000)

print(insertion_sort(my_array))

print("***********************************************************")

my_array = generate_array(10000)

print(insertion_sort(my_array))

print("***********************************************************")

my_array = generate_array(100000)

print(insertion_sort(my_array))

print("***********************************************************")
