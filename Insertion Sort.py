
import random


def random_nums(length=1, min_val=0, max_val=10000):
    arr = []
    for i in range(length):
        arr.append(random.randint(min_val, max_val))
    return arr

def insert_sort(arr):
    
##  Start at index of 1.
    for i in range(1, len(arr)):

##  Current value of index.    
        j = arr[i]
        
##  While loop that moves sorted index values greater than current value 1 step to right
        k = i-1

        while k >= 0 and j < arr[k]:
            arr[k+1] = arr[k]
            k -= 1

        arr[k+1] = j

arr = []

arr = random_nums(50)

print("Unsorted array:", arr)

insert_sort(arr)

print("Sorted array:", arr)
