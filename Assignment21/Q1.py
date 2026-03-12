import threading

def PrimeNums(Value):
    PNo = []
    for i in Value:
        isPrime = True
        for j in range(2, i//2+1):
            if(i % j == 0):
                isPrime = False
        
        if(isPrime):
            PNo.append(i)
    print("Prime Number :",PNo)



def notPrime(Value):
    NPno = []

    for i in Value:
        isPrime = True
        for j in range(2, i //2+1):
            if(i % j == 0):
                isPrime = False

        if(isPrime == False):
            NPno.append(i)
    print("Non Prime Number :",NPno)


def main():
    print("Enter Number of Elements :")
    No = int(input())

    Data = []
    print("Enter Elements :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)

    PrimeNums = threading.Thread(target=PrimeNums,args=(Data,))
    notPrime = threading.Thread(target=notPrime,args=(Data,))

    PrimeNums.start()
    notPrime.start()
    PrimeNums.join()
    notPrime.join()


if __name__ == "__main__":
    main()

