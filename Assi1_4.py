# This Code is the Ans of 3,4,5 question of Assignment NO 9
import multiprocessing
import time
import os
def Cube(No):
    Ans = 0
    for i in range(1,No+1):
        Ans = i**3

    return Ans

def SQRT(No):
    Ans = 0
    for i in range(1,No+1):
        Ans = i**2
    
    return Ans

def CheckDivisible(No):
    if (No % 3 == 0) and (No % 5 == 0):
        print("No is Divisible by 3 and 5 ")
    
    else:
        print("No is not Divisible by 3 and 5")
    


def main():
    Value = 0
    Ret = 0

    start_time = time.time()
    Value = int(input("Enter the No.:"))

    Ret = Cube(Value)
    print("Cube of No :",Ret)

    Ret = SQRT(Value)
    print("SQRT of No :",Ret)

    CheckDivisible(Value)    
    end_time = time.time()
    print("Time Required :",end_time - start_time)

    
    
if __name__=="__main__":
    main()