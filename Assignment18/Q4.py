# Accept List and and accept another number input which we wnat to Check how many times occures in list

def CheckFrequency(Element,Num):
    Cnt  = 0
    for i in Element :
        if (i == Num):
            Cnt = Cnt + 1
        
    return Cnt    

def main():
    size = 0
    Value = 0    
    Ret = 0
    print("Enter the number of element :")
    size = int(input())

    Data = list()
    print("Enter the element :")
    for i in range(size):
        Value = int(input())
        Data.append(Value)
    
    No = int(input("Enter Number Which u want to Check :"))

    
    Ret = CheckFrequency(Data,No)
    print("Number Occurance :",Ret,"Times")


if __name__ =="__main__":
    main()
