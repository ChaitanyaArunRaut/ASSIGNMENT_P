# write lamda functionn using filter 
# check list of number is divisible by 3 and 5
from functools import reduce
def Divisible(No):
    return (No % 3 ==0) and (No % 5 == 0)
CheckDivisible = lambda Element : list(filter(Divisible,Element))
def main():
    No = int(input("Enter the number of element in list :"))
    Data = list()
    print("Enter Elements in list :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)
    print("Elements in list is :",Data)

    fData = CheckDivisible(Data)
    print("Data divisible by 3 and 5 is :",fData)

if __name__=="__main__":
    main()