# write a lambda function using Reduce()
# accept the list from user and return minimum Elemt
from functools import reduce
def MaximumNum(No1, No2):
    if(No1 > No2):
        return No2
    else:
        return No1
    
Maximum  = lambda No : int(reduce(MaximumNum,No))

def main():
    No = int(input("Enter the number of element in list :"))
    Data = list()
    print("Enter Elements in list :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)
    print("Elements in list is :",Data)

    Result = Maximum(Data)
    print("Minimum Result :",Result)

if __name__=="__main__":
    main()