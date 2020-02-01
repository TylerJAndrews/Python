

num = list(input("Put potential credit card number here: "))


def verify_cc(num):

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

print(verify_cc(num))
