# contains one lambda function accept two parameters and returns its multiplication.
# Write a program  which contains one lambda function which accept one parameter and return power of two
Power = lambda Num1, Num2 : Num1 * Num2
def main():
    No1 = int(input("Enter First Numbers :"))
    No2 = int(input("Enter Second Number :"))
    Ret = 0

    Ret = Power(No1,No2)
    print("Power of Number is :",Ret)

if __name__ == "__main__":
    main()