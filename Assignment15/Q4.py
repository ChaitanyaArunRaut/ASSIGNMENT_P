# write a lambda function using Reduce()
# accept th list of numbers and returns the add of all elemets 
from functools import reduce
Add = lambda No1, No2 : No1 + No2
def main():
    No = int(input("Enter the number of element in list :"))
    Data = list()
    print("Enter Elements in list :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)
    print("Elements in list is :",Data)

    Rdata = reduce(Add,Data)
    print("Data after Reduce is :",Rdata)


if __name__=="__main__":
    main()