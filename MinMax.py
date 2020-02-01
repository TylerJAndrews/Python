

arr = [2, 5, 1, 4, 10, 7]

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
            
    return minimum, index_min, maximum, index_max

    
print(arr)

print(min_max(arr))
