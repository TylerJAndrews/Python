import random

def random_nums(qty = 1, min_val=0, max_val=10000):
    
    arr = []
    
    for i in range(qty):
        arr.append(random.randint(min_val, max_val))
        
    return arr

def verify_cc(num):
    
    num = str(num)
    num = list(map(int,num))[::-1]

    for i in range(1,len(num),2):
        if num[i] < 5:
            num[i] = num[i] * 2
        else:
            num[i] = ((num[i] * 2)//10) + ((num[i] * 2)%10)

    num_sum = sum(num) 

    if num_sum%10 != 0:
        valid = False
    else:
        valid = True

    return valid

def generate_ccnum(qty = 1):
    if qty == 0:
        return
    
    maybe = random_nums(1, 1000000000000000, 9999999999999999)[0]
    valid = verify_cc(maybe)

    if valid == False:
        generate_ccnum(qty)
    else:
        print("Your new CC number is:", maybe)
        generate_ccnum(qty-1)

generate_ccnum()
