#accept one Num andd return true if number is Odd otherwise false
Maximum = lambda No : False if No % 2 == 0 else True

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter Number :"))

    Ret = Maximum(Value)
    print("Its",Ret)    

if __name__=="__main__":
    main()