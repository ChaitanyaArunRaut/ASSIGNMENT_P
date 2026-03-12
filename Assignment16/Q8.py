# print * * * * * on screen n times 

def display(Num):
    for i in range(Num):
        print("*",end=" ")

def main():
    No = int(input("Enter Number of times to Display :"))
    display(No)
if __name__ == "__main__":
    main()
    