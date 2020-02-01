

arr = [2, 5, 1, 4, 10, 7]
sorted_arr = []

def min_max(arr):

    maximum   = None
    index_max = None
    minimum   = None
    index_min = None
    
    for i, val in enumerate(arr):


        if maximum == None or val > maximum:

            maximum = val
            index_max = i

         
        if minimum == None or val < minimum:
            
            minimum = val
            index_min = i
            
    return index_min, minimum, index_max, maximum

print(arr)

print(sorted_arr)

for i in range(len(arr)):

    index_min, minimum, _ , _ = min_max(arr)
    
    sorted_arr.append(minimum)
    
    arr.pop(index_min)

pass
  
print(arr)

print(sorted_arr)
