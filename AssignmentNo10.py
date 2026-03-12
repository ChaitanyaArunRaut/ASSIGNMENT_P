# print the Table of Number 
def Table(No):
    Ans = 0
    for i in range(1, 11):
       Ans=i*No
       print(Ans)
       
# print sum of n natural number 5 - 11+2+3+4+5 = 15 
def Add(No):
    Sum = 0
    for i in range(1,No+1):
        Sum+=i
    return Sum

# Print the factorial of No
def Factorial(No):
    Result = 1
    for i in range(1,No+1):
        Result = Result* i 
    return Result

#print Even Numbers from No
def Even(No):
    for i in range (2, No+1,2):
        if i % 2 ==0:
            print("Even No is :",i)
        
# print Odd Number from No
def ODD(No):
    for i in range(1,No+1,2):
        if i % 2==0:
            return
        else:
            print("ODD No is :",i)
                           
def main():
    Value = None
    Ret = 0
    Value =int(input("Enter the No. :"))

    Table(Value)
    Ret = Add(Value)
    print("Addition of natural Number is :", Ret)

    Ret = Factorial(Value)
    print("Fatorial of NO is  :",Ret)

    Even(Value)
    ODD(Value)

if __name__=="__main__":
    main()