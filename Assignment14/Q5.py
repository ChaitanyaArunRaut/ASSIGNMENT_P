#accept one Num andd return true if number is even otherwise false
Maximum = lambda No : True if No % 2 == 0 else False
def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter Number :"))

    Ret = Maximum(Value)
    print("Its",Ret)    

if __name__=="__main__":
    main()