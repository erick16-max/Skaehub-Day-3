import numpy as np
def size_of_array():
    #num = int(input("Number of elements in the array: "))
    arr = np.array(list(map(int, input("Elements of the array: ").strip().split())))
    arr_size = arr.size
    memory_occupied = arr.size*arr.itemsize
    return arr, arr_size, memory_occupied 

