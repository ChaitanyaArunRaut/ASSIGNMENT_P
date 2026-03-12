# filter(), map(), reduce()
# accept number in list from user 
# filter = collect even nums
# map = calculate even nums squre
# reduce = return addition of square nums 

from functools import reduce
def CheckEven(Num):
    return Num % 2 == 0        

def SQRTEven(Num):
    return Num**2

def AddSQRT(No1, No2):
    return No1 + No2

def FMR(GrpNo):
    
    FData = list(filter(CheckEven,GrpNo))
    print("'Data after filter is :",FData)

    MData = list(map(SQRTEven,FData))
    print("Data after Map :",MData)

    RData = int(reduce(AddSQRT,MData))
    print("Data after the Reduce is :",RData)


def main():
    No = int(input("How many number you want to input in list : "))

    Data = []

    for i in range(No):
        Elements = int(input("Enter Numbers in list :"))
        Data.append(Elements)

    print("Number of Elements in a list :",Data)

    FMR(Data)

if __name__ == "__main__":
    main()