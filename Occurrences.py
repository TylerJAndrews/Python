

array = [2, 3, 1, 1, 4, 3, 4, 1, 3, 2, 1]
string = 'appliedapplealleged'

def instances(arr, val):

    count = 0

    for value in arr:

        if value == val:

            count = count + 1

    return count

print(array)

print(instances(array, 5))

print(string)

print(instances(string,'d'))


