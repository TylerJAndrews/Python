
a = [1,2,3,4]
b = [5,6,7,8]


def swapverse(arr1, arr2):

    temp = [val for val in arr1]
    length = len(arr1)
        
    for i in range(len(arr2)):
        arr1.append(arr2.pop())
        
        
    for i in range(length):
        arr2.insert(0, arr1.pop(0))
        
    
swapverse(a,b)
print(a)
print(b)





        

    
