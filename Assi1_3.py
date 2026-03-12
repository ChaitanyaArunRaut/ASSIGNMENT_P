def SQRT(Value):
    Ans = 0
    Ans = Value*Value
    return Ans
    
def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter the Number :"))
    Ret = SQRT(Value)

    print("Square root of No is :",Ret)


if __name__=="__main__":
    main()