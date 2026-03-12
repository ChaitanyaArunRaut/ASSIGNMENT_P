# Accept one Number and return its Factorial
def Factorial(No):
    Ans = 1
    for i in range(No, 0, -1):
        Ans = Ans * i
    return Ans
 
def main():
    Ret = 0
    Num = int(input("Enter Number to find Factorial :"))
    Ret = Factorial(Num)
    print("Factorial is :",Ret)
    
if __name__ == "__main__":
    main()