# accept the list of number and check even and return addition of even numbers
from functools import reduce
def Add(A, B):
   return A + B

CheckEven = lambda NO : True if (NO % 2 ==0) else False

def main():
    No = int(input("Number of Element in list :"))
    Data = list()
    print("Enter elemets in List :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)

    print("Elements in list is :",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after Filter :",FData)

    RData = reduce(Add,FData)
    print("Data after Reduce is :",RData)
   
if __name__=="__main__":
    main()