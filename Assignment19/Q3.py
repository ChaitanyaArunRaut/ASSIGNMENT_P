#Contains Filter(), map() and reduce()
# contains one list accept from user and filter filter out all such number which is greater that or equal to 70 and less than equal to 90
# map increase the number by 10
# return the produc of all numbers
from functools import reduce
def CheckFilter(Num):
    return  Num >= 70 and Num <= 90
    
def Increment(Num):
    return Num + 10

def Product(No1,No2):
    return No1 * No2

def FilterMapReduce(GrpNum):
    FData = list(filter(CheckFilter,GrpNum))
    print("Data After Filter is ;",FData)

    Mdata = list(map(Increment,FData))
    print("Data after maping is :",Mdata)

    RData = int(reduce(Product,Mdata))
    print("Data after reduce is :",RData)

def main():
    NO = int(input("Enter Number of inputs you want :"))
    Data = list()
    for i in range (NO):
        Element = int(input("Enter Numbers in List :"))
        Data.append(Element)

    print("List of Numbers is :",Data)

    FilterMapReduce(Data)

if __name__=="__main__":
    main()