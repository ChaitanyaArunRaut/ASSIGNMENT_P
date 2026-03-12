# Write a program  which contains one lambda function which accept one parameter and return power of two
Power = lambda num : num **2
def main():
    No1 = int(input("Enter First Numbers :"))
    Ret = 0

    Ret = Power(No1)
    print("Power of Number is :",Ret)

if __name__ == "__main__":
    main()