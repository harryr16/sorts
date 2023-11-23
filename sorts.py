
import random

def create_test_list(size):
    ints_list = []
    for i in range(size):
        ints_list.append(random.randint(-size, size*2))
    return ints_list

def bubble_sort(arr):
    pass

ints_list = create_test_list(10)
print("Items to sort: ", ints_list)
#print("Bubble sorted: "+bubble_sort(ints_list))