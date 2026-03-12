# Accept 2 numbers and return its addition
Addition = lambda No1, No2 : No1 + No2

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter first Number :"))
    Value2 = int(input("Enter Second Number:"))

    Ret = Addition(Value1, Value2)
    print("Addition is :",Ret)    

if __name__=="__main__":
    main()