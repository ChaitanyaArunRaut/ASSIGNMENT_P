#Accept n numbers fromm user and store it into list. 
# Return Maximum Num

def Max(Element):
    Max = float('-inf')
    for i in Element:
        if(i > Max):
            Max = i
        
    return Max

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
    
    Ret = Max(Data)
    print("Maximum No is  :",Ret)


if __name__ =="__main__":
    main()
