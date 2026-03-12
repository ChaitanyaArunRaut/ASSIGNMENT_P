# filter(), map(), reduce()
# filter = collect prime numbers 
# map() = multiply by 2
# reduce() = Return maximum 
from functools import reduce

def CheckPrime(Num):
    isPrime = True
    for i in range(2,(Num//2)+1):
        if(Num % i == 0):
            isPrime = False
    
    return isPrime

def Mult(Num):
    return Num * 2
    
def RMax(No1, No2):
    return max(No1,No2)

def FMR(GrpNum):
    FData = list(filter(CheckPrime,GrpNum))
    print("Data After filter is :",FData)

    MData = list(map(Mult,FData))
    print("Data after map : ",MData)

    RData = int(reduce(RMax,MData))
    print("Data after Reduce is :",RData)

def main():

    No = int(input("Enter Number you want to input :"))

    Data = list()

    for i in range(No):
        Element = int(input("Enter the Data in list :"))
        Data.append(Element)

    print("Data of list :",Data)

    FMR(Data)


if __name__ == "__main__":
    main()
    