from MarvellousNum import CheckPrime


def main():
    No = int(input("Enter Number of Elements :"))
    Data = list()
    Ret = 0
    print("Enter N Elements in list :")
    for i in range(No):
        Elements = int(input())
        Data.append(Elements)

    print("Number of Elments in List :",Data)

    Ret = CheckPrime(Data)
    print("Addition of Prime Numbers is :",Ret)

if __name__ == "__main__":
    main()