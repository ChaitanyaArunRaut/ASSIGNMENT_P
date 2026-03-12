#Check Wheter number is Prime or not 

def CheckPrime(No):
    if No <= 1:
        return False
    
    for i in range(1, No//2 +1):
        if (No % 2 == 0):
            return False
        else:
            return True


def main():
    Value = int(input("Enter Number :"))
    Ret = 0
    Ret = CheckPrime(Value)
    if Ret == True:
        print("Number is Prime")
    else:
        print("Number is not Prime")


if __name__ =="__main__":
    main()