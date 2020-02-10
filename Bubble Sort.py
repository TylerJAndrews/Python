
import random


def random_nums(length=1, min_val=0, max_val=10000):
    arr = []
    for i in range(length):
        arr.append(random.randint(min_val, max_val))
    return arr

def bubble_sort(arr):
    
    comp = 0
    
    for i in range(len(arr)):
        updated = False
        
        for j in range(len(arr)-i-1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                updated = True
        if not updated:
            break
    return comp


arr = random_nums(10000)

print(bubble_sort(arr))
print(arr)
