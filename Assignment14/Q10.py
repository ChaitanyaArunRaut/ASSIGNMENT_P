#Accept 2 numbers and returns Multiplication
Multiplication = lambda No1,No2,No3 : max(No1,No2,No3)

def main():
    Value1 = 0
    Value2 = 0
    Value3 = 0
    Ret = 0

    Value1 = int(input("Enter first Number :"))
    Value2 = int(input("Enter Second Number:"))
    Value3 = int(input("Enter Third Number:"))

    Ret = Multiplication(Value1, Value2,Value3)
    print("Largest Number is :",Ret)    

if __name__=="__main__":
    main()