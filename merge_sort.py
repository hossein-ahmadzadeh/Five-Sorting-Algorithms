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
def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2

        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return arr


my_array = generate_array(1000)

print(merge_sort(my_array))

print("***********************************************************")

my_array = generate_array(10000)

print(merge_sort(my_array))

print("***********************************************************")

my_array = generate_array(100000)

print(merge_sort(my_array))

print("***********************************************************")
