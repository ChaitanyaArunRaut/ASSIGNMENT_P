# this code contains the special Function as lambda

Addition = lambda No1, No2 : No1 + No2

Substraction = lambda No1, No2 : No1 - No2

Multiplication = lambda No1, No2 : No1 * No2

Division = lambda No1, No2 : No1 / No2


def main():
    Value1 = int(input("Enter the First Number :"))
    Value2 = int(input("Enter the Second Number :"))
    Ret = 0

    Ret = Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Substraction(Value1,Value2)
    print("Substration is :",Ret)

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Division(Value1,Value2)
    print("Division is :",Ret)

if __name__=="__main__":
    main()