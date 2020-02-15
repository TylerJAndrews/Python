
def permute(arr, shape):

    new_arr = []
    
    for i in range(len(arr)):
        new_index = shape[i]
        
        if new_index == None or new_index >= len(arr):
            new_arr.append(None)
        else:
            new_arr.append(arr[new_index])
        
    return new_arr

print(permute([1,2,3,4,5], [None,0,3,4,17]))
