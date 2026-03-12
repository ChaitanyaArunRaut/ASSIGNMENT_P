# check Num divisible by 5 or not 
def CheckNum(No):
    if(No % 5 == 0):
        return True
    else:
        return False
          
def main():
    Num = int(input("Enter Number :"))
    Ret = 0
    Ret = CheckNum(Num)
    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()