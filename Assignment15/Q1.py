# Write a lambda function using map() which accept list of numbers and returns a list of square of each number.

SqureRoot = lambda No : (No*No)

def Mapx(Task, Element):
    Result = list()

    for No in Element:
        Ret = Task(No)
        Result.append(Ret)
    
    return Result

def main():
    No = int(input("Number of Element in list :"))
    Data = list()
    print("Enter elemets in List :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)

    print("Elements in list is :",Data)

    MData = list(Mapx(SqureRoot,Data))
    print("Data after Maping is :",MData)
    
if __name__=="__main__":
    main()