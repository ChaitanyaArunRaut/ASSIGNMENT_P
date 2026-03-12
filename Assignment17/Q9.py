# Write a programe which accept Number form user and retrun number of Digits in that number.

def Count(No):
    Count = 0
    while( No > 0):
        Count = Count+1
        No = No//10
    return Count

def main():
    Num = int(input("Enter Any Number :"))
    Ret = 0

    Ret = Count(Num)
    print("The Length of Number is :",Ret)

if __name__ == "__main__":
    main()