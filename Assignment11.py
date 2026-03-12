# Check Whether  Number us Prime or not 
def CheckPrime(No):
   if No > 0:
       for i in range (2,No):
            if No % i==0:
                print("Number is NOT Prime")
            else:
                print("Number is  prime")
            break
       
# accept one no and prit the count of the number 
def CountDigit(No):
    Count = 0
    while No > 0:
        No = No // 10
        Count= Count+1 
    return Count

# Accept one No and count and print count of digit of that no
def SumDigit(No):
    total = 0

    while No > 0:
        Digit = No % 10
        total = total + Digit
        No = No // 10 # flore Division 123 / 10 = 12.30 and it kept only 12
    return total

# Reverse the No
def Reverse(No):
    Rev = 0
    while No > 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10
    return Rev

# Check NO is Palindrome or not (No read the forword and Backword same)
# EX 121,1331
def CheckPalindrome(No):
    Value = No
    Rev  = 0
    while No > 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10
    if(Value == Rev):
        print(Rev,"The Given Number is Palindrome :")
    else:
        print(Rev,"The Given Number is not Palindrome")

def main():

    Value = 0
    Ret = 0
    Value = int(input("Enter the Number :"))

    CheckPrime(Value)

    Ret = SumDigit(Value)
    print("Addition of Digits is :",Ret)

    Ret = CountDigit(Value)
    print("No of Digit is :",Ret)

    Ret = Reverse(Value)
    print("Reverse No is :",Ret)

    CheckPalindrome(Value)



if __name__=="__main__":
    main()