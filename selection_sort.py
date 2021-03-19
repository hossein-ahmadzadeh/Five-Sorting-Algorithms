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
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


my_array = generate_array(1000)

print(selection_sort(my_array))

print("***********************************************************")

my_array = generate_array(10000)

print(selection_sort(my_array))

print("***********************************************************")

my_array = generate_array(100000)

print(selection_sort(my_array))

print("***********************************************************")
