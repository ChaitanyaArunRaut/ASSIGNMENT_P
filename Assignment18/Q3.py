#Accept n numbers fromm user and store it into list. 
# Return Minimum Num

def Min(Element):
    Min = float('inf') # Positive infinity for Negative use float ('-inf')
    for i in Element:
        if(i < Min):
            Min = i
        
    return Min

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
    
    Ret = Min(Data)
    print("Minimum No is  :",Ret)


if __name__ =="__main__":
    main()
