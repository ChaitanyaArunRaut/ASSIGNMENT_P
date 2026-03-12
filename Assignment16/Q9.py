# Write a Programe which Display first 10 Even Numbers on screen. 
def Even(No):
    Count = 0
    Num = 1

    while(Count < No):
        if(Num % 2 == 0):
            print(Num)
            Count = Count + 1
        Num += 1

def First10Even(No):
        for i in range(1, No+1):
             i = i * 2
             print(i)
        

def main():
   
   Value = 10
   print("First 10 Even Numbers using while Loop :")
   Even(Value)
   print("First 10 Even Numbers using for loop:")
   First10Even(Value)
if __name__ == "__main__":
    main()