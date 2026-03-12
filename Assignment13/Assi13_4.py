#accept number and prints binery equivalent
def Binery(No):
    Bny = ""
    if No == 0:
        Bny = 0
    while No > 0:
        Remainder = No % 2
        Bny = str(Remainder)+Bny
        No = No // 2
    return Bny
    
def main():
    value = int(input("Enter a Number :"))
    Ret = 0
    Ret = Binery(value)
    print("Binary Equivalnet is :",Ret)

if __name__=="__main__":
    main()