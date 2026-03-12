
CheckEven = lambda No : (No % 2 == 0) 

def FilterX(Task, Element):
    Result = list()

    for No in Element:
        Ret = Task(No)
        
        if(Ret == True):
            Result.append(No)
    
    return Result

def main():
    No = int(input("Number of Element in list :"))
    Data = list()
    print("Enter elemets in List :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)

    print("Elements in list is :",Data)

    fData = list(FilterX(CheckEven,Data))
    print("Data after Filter is :",fData)
    
if __name__=="__main__":
    main()