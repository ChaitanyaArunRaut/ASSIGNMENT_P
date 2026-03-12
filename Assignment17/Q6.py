# Display Patern 

def Display(No):
    for i in range(No, 0, -1):
        for j in range(i, 0 ,-1):
            print("*",end = " ")
        print()

def Display2(No):
    for i in range(1, No+1, 1):
        for j in range(1, i+1, 1):
            print("*",end = " ")
        print()
def main():
    Value = int(input("Enter Number of Rows :"))
    Display(Value)
    Display2(Value) 

if __name__ =="__main__":
    main()