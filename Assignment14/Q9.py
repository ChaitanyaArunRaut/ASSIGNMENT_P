#Accept 2 numbers and returns Multiplication
Multiplication = lambda No1, No2 : No1 * No2

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter first Number :"))
    Value2 = int(input("Enter Second Number:"))

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is :",Ret)    

if __name__=="__main__":
    main()