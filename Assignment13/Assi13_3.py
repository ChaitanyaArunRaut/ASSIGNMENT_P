# Check the Number is Perfect or not 
# 6 - 1+2+3 = 6
def CheckPerfect(No):
    Sum = 0
    for i in range (1, No):
        if No % i == 0:
            Sum = Sum + i
    if Sum == No:
        print("Number is perfect ")
    else:
        print("Number not perfect")

def main():
    Value = int(input("Enter the Number :"))

    CheckPerfect(Value)
if __name__=="__main__":
    main()