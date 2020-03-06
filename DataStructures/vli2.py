
class VeryLargeInt:

    def __init__(self,):
        self.arr = []

    def add_int(self, num):
        self.arr.append(num)

    def __add__(self, other = [0]):
        other = other[::-1]
        rra   = self.arr[::-1]
        if len(other) > len(rra):
            rra, other = other, rra
        
        carry = 0
        for i in range(len(other)):
            rra[i] = rra[i]+ other[i]
        
        length = len(rra)
        for i in range(length):
            rem   = rra[i]%10
            carry = int(rra[i]//10)

            rra[i] = rem
            try:
                rra[i+1] = rra[i+1] + carry
            except IndexError: 
                if carry:
                    rra.append(carry)
            # print(rra)
        self.arr = rra[::-1]
        # print(self.arr)
        return self 
    
    def __mul__(self, other = 1):
        plus = self.arr
        self.arr = [0]
        for i in range(other):
            self = self + plus
        return self

    def __str__(self,):
        arr = self.arr

        string = ''
        for i in range(len(arr)):
            string += str(arr[i])
        return string

    @staticmethod
    def factorial(num):
        vli = VeryLargeInt()
        vli.add_int(1)
        for i in range(2,num+1):
            vli = vli * i
            print(i)
        return vli

print(VeryLargeInt.factorial(1000))