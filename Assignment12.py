# Check the character is Vowel or Not
def CheckVowel(ch):
    if ch.lower() in ['a','e','i','o','u']:
        print(ch,"it is a vowel")
    else:
        print(ch,"it is not vowel")

# accept one no and print its factors  12 = 1,2,3,4,6,12
def Factors(No):
    for i in range(1,No+1):
        if No % i == 0:
            print("Factors of the Number is :",i)

# Accept the input and show from its starting 5 = 1 2 3 4 5
def Number(No):
    for i in range (1, No+1):
        print(i)

#Accept the input and show from its Ending 5 = 5 4 3 2 1
def RNumber(No):
    for i in range(No, 0, -1):
        print(i)

def main():
    
    char = (input("Enter the Character :"))

    Value = 0
    Value = int(input("Enter the Value :"))

    CheckVowel(char)
    Factors(Value)
    Number(Value)
    RNumber(Value)

if __name__=="__main__":
    main()