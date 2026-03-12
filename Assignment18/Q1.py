# write a program which accept N numbers from user and store it into list.
# Return addition of all elements from that List.

def Additon(Element):
    Sum = 0
    for i in range(len(Element)):
        Sum = Sum + Element[i]
    
    return Sum

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
    
    Ret = Additon(Data)
    print("Sumation of :",Ret)


if __name__ =="__main__":
    main()
