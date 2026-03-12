# accept number and check whether number is positive or negative or zero

def CheckNum(No):
    if(No > 0):
        print("Positive Number :")
    elif(No < 0):
        print("Negative Number :")
    else:
        print("Zero :")
        
def main():
    Num = int(input("Enter Number :"))
    CheckNum(Num)

if __name__ == "__main__":
    main()