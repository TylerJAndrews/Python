

array = [2, 3, 1, 1, 4, 3, 4, 1, 3, 2, 1]
string = 'appliedapplealleged'

def instances(arr, val):

    count = 0

    for value in arr:

        if value == val:

            count = count + 1

    return count

def frequencies(arr, vals):

    if len(vals):

     val = vals.pop(0)
     
     return [instances(arr, val)] + frequencies(arr, vals)
    
    return []

print(frequencies(array, [1, 2, 3, 4]))


##print(array)
##
##print(instances(array, 5))
##
##print(string)
##
##print(instances(string,'d'))


