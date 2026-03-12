# Accept One number and return the addition of each no

def AddNum(No):
    Ans = 0 
    while(No > 0):
        RValue = No % 10
        Ans +=RValue
        No = No // 10
    return Ans


def main():
    Num = int(input("Enter Any Number :"))
    Ret = 0

    Ret = AddNum(Num)
    print(" Additon of Numbers is :",Ret)

if __name__ == "__main__":
    main()