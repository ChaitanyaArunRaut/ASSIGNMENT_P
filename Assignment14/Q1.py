# Calculate the Square root of the number 
SQRT = lambda No : (No*No)
def main():
    Value = 0
    Value = int(input("Enter the Number :"))
    Ret = 0
    Ret = SQRT(Value)
    print("Square Root is :",Ret)

if __name__=="__main__":
    main()

    