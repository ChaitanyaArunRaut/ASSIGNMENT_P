PI = 3.14
print("Inside Module :",__name__)
def CheckPrime (Num):
    Sum = 0
    for n in Num:
        if n > 1:
            isPrime = True
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    isPrime = False
                    break

            if isPrime:
                Sum = Sum + n
    return Sum


    