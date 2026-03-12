def Display():
    print("Jay Ganesh...")

def ChkGreater(No1, No2):
    if (No1 > No2):
        print("Greater Value is:",No1)
    else:
        print("Greater Vaue is :",No2)    
         
def main():

    Value1 = 0
    Value2 = 0
    Ret = None

    Value1 = int(input("Enter First No :"))
    Value2 = int(input("Enter First No :"))
    Display()
    ChkGreater(Value1,Value2)

if __name__=="__main__":
    main()