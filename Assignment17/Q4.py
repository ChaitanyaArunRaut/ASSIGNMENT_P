# accept one number and return addition of factors of that number 
def AddFact(No):
    Sum = 0
    for i in range(1, No//2+1):
        if (No % i ==0):
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter Number : "))
    Ret = 0

    Ret = AddFact(Value)
    print("Addition of Factors is :",Ret)

if __name__ == "__main__":
    main()